import threading
from app import create_app, socketio
from app.main.events import send_periodic_messages

app = create_app(debug=True)

if __name__ == '__main__':
    thread = threading.Thread(target=send_periodic_messages)
    thread.daemon = True
    thread.start()
    socketio.run(app, host='0.0.0.0', port=8080, debug=True, use_reloader=False)
    # socketio.run(app)
