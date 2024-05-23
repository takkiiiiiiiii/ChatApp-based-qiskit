from concurrent.futures import thread
import hashlib
import threading
import time
from flask import session, request
from flask_socketio import emit, join_room, leave_room, send, Namespace
from .. import socketio
# import threading
from app.main.qkd import bb84
import pickle

# global_data_lock = threading.Lock()
room_user_count = 0
room_users = []
client_rooms = {}

len_key = 2048
num_qubits = 23

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

@socketio.on('joined', namespace='/chat')
def joined(message):
    global room_user_count  # この行を追加
    global room_users
    global users
    
    
    # room = request.sid  # SocketIOのセッションIDを使ってroomを識別

    # username = message.get('name')  # フロントからのメッセージに含まれるユーザー名を取得

    # room = session.get('room')
    room = session.get('room')
    username = session.get('name')
    join_room(room)

    if username not in room_users:
        u = User(username, any, any, any)
        users.append(u)
        room_users.append(username)
        room_user_count += 1
    
    if room_user_count == 2:
        user0 = users[0]
        user1 = users[1]
        current_sender_key = ''
        current_receiver_key = ''

        sender_key_part, receiver_key_part = bb84(user0, user1, num_qubits) # create a part of shareKey

        # while len(current_sender_key) <= len_key:
        #     current_sender_key += sender_key_part
        #     current_receiver_key += receiver_key_part

        user0.sharekey = current_sender_key
        user1.sharekey = current_receiver_key
        hash_key = hashlib.sha256(current_receiver_key.encode())
        emit('status', {'msg': session.get('name') + ' has entered the room.', 'room_user_count' : room_user_count, 'sharekey' : hash_key.hexdigest()}, room=room)
        return

    emit('status', {'msg': session.get('name') + ' has entered the room.', 'room_user_count' : room_user_count}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    # room = request.sid
    room = session.get('room')
    # room = message.get('room')
    user0 = users[0]
    user1 = users[1]
    usernames = [user0.username, user1.username]

    ciphertext = []
    plaintext = message['msg']

    

    binary_representation = ''.join(format(ord(char), '08b') for char in plaintext)
    ciphertext = [0] * len(binary_representation)
    for i in range(len(binary_representation)):
        ciphertext[i] = int(binary_representation[i]) ^ int(user0.sharekey[i])
    
    binary_representation_plaintext = [0] * len(ciphertext)
    
    for i in range (len(ciphertext)):
        binary_representation_plaintext[i] = int(ciphertext[i]) ^ int(user1.sharekey[i])

    plaintext = ''
    for i in range(0, len(binary_representation_plaintext), 8):
        byte = binary_representation_plaintext[i:i+8]
        byte_value = int(''.join(map(str, byte)), 2)
        plaintext += chr(byte_value)

    # discard the sharekey and create new sharekey (onetimepad)
    sender_key_part, receiver_key_part = bb84(user0, user1, num_qubits, len_key)
    current_sender_key = ''
    current_receiver_key = ''
    while len(current_sender_key) <= len_key:
            current_sender_key += sender_key_part
            current_receiver_key += receiver_key_part

    user0.sharekey = current_sender_key
    user1.sharekey = current_receiver_key
    print(len(current_receiver_key))

    hash_key_for_user0 = hashlib.sha256(current_sender_key.encode())
    hash_key_for_user1 = hashlib.sha256(current_receiver_key.encode())

    
    emit('message', {'msg': session.get('name') + ':' + plaintext, 'sender' : session.get('name'), 'updatekey' : hash_key_for_user0.hexdigest(), 'usernames' : usernames}, room=room)

    
# @socketio.on('server_request', namespace='/chat')


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

