from concurrent.futures import thread
import hashlib
import threading
import time
from flask import session, request
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from app.main.generate_sharekey import Generate_Key, Generate_Key_Join
import random

key_lock = threading.Lock()



room_user_count = 0
room_users = []
client_rooms = {}

current_sender_key = ''
current_receiver_key = ''

len_key = 1008
interval = 90


class User:
    def __init__(self, username: str, sharekey, socket_classical, socket_quantum):
        self.username = username
        self.sharekey = sharekey
        self.socket_classical = socket_classical
        self.socket_quantum = socket_quantum

    def create_socket_for_classical(self):
        import socket
        SERVER_HOST_CLASSICAL = '127.0.0.1'
        SERVER_PORT_CLASSICAL = 12001
        client_socket_classical = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket_classical.connect((SERVER_HOST_CLASSICAL, SERVER_PORT_CLASSICAL))
        self.socket_classical = client_socket_classical        


users = []

def update_key():
    global current_sender_key, current_receiver_key
    print(room_user_count)
    key_generator = Generate_Key(users[0], users[1], len_key)
    key_generator.start()   
    while True:
        time.sleep(interval)
        current_sender_key = key_generator.sender_key
        print(f'Current Key: {current_sender_key}')
        current_receiver_key = key_generator.receiver_key
        hash_key_for_user0 = hashlib.sha256(current_sender_key.encode())
        hash_key_for_user1 = hashlib.sha256(current_receiver_key.encode())
        socketio.emit('update_key', {'updatekey': hash_key_for_user0.hexdigest(), "interval": interval}, namespace='/chat')


@socketio.on('joined', namespace='/chat')
def joined(message):
    global room_user_count
    global room_users
    global users
    global current_sender_key, current_receiver_key
    
    room = session.get('room')
    username = session.get('name')
    join_room(room)
    if username not in room_users:
        u = User(username, None, None, None)
        users.append(u)
        room_users.append(username)
        room_user_count += 1
    
    if room_user_count == 2:
        key_generator = Generate_Key_Join(users[0], users[1], len_key)
        reconciled_key = key_generator.gen_key_joined()
        current_sender_key = reconciled_key
        current_receiver_key = reconciled_key
        print(f'First current_sender_key : {current_sender_key}')
        sender_hash_key = hashlib.sha256(current_receiver_key.encode())
        receiver_hash_key = hashlib.sha256(current_receiver_key.encode())
        emit('status', {'msg': session.get('name') + ' has entered the room.', 'room_user_count' : room_user_count, 'sharekey' : sender_hash_key.hexdigest(), "interval": interval}, room=room)

        socketio.start_background_task(update_key)
        return

    emit('status', {'msg': session.get('name') + ' has entered the room.', 'room_user_count' : room_user_count}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    global current_sender_key, current_receiver_key

    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    user0 = users[0]
    user1 = users[1]
    usernames = [user0.username, user1.username]

    ciphertext = []
    plaintext = message['msg']

    binary_representation = ''.join(format(ord(char), '08b') for char in plaintext)
    ciphertext = [0] * len(binary_representation)
    for i in range(len(binary_representation)):
        ciphertext[i] = int(binary_representation[i]) ^ int(current_sender_key[i])
    
    binary_representation_plaintext = [0] * len(ciphertext)
    
    for i in range (len(ciphertext)):
        binary_representation_plaintext[i] = int(ciphertext[i]) ^ int(current_receiver_key[i])

    plaintext = ''
    for i in range(0, len(binary_representation_plaintext), 8):
        byte = binary_representation_plaintext[i:i+8]
        byte_value = int(''.join(map(str, byte)), 2)
        plaintext += chr(byte_value)

    user0.sharekey = current_sender_key
    user1.sharekey = current_receiver_key
    print(f'Plaintext: {plaintext}')
    
    emit('message', {'msg': session.get('name') + ':' + plaintext, 'sender' : session.get('name'), 'usernames' : usernames}, namespace='/chat', room=room)






@socketio.on('left', namespace='/chat')
def left(message):
    global room_user_count  # この行を追加
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    # room = message.get('room')
    room_user_count -= 1
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

