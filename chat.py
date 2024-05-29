import threading
from app import create_app, socketio
from app.main.events import update_key


app = create_app(debug=True)

if __name__ == '__main__':
    socketio.start_background_task(update_key)
    socketio.run(app, host='0.0.0.0', port=8080, debug=True, use_reloader=False)
