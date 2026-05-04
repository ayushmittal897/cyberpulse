from backend.app import create_app, socketio
from config import Config

app = create_app()

if __name__ == '__main__':
    print(f"[*] Starting CyberPulse on port {Config.PORT}")
    socketio.run(app, host='0.0.0.0', port=Config.PORT, debug=Config.DEBUG)
