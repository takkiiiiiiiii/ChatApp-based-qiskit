import threading
from app import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
   
    socketio.run(app, host='0.0.0.0', port=8080, debug=True, use_reloader=False)
    # socketio.run(app)
