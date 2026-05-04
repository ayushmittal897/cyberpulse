from flask import Flask, render_template
from flask_socketio import SocketIO
from config import Config
import os

socketio = SocketIO(cors_allowed_origins=Config.CORS_ALLOWED_ORIGINS)

def create_app():
    # Setup paths so Flask finds static/templates correctly
    base_dir = os.path.abspath(os.path.dirname(__file__))
    frontend_dir = os.path.join(base_dir, '../frontend')
    
    app = Flask(
        __name__,
        template_folder=os.path.join(frontend_dir, 'templates'),
        static_folder=frontend_dir,
        static_url_path='/static'
    )
    app.config.from_object(Config)

    socketio.init_app(app)

    # Register Blueprints
    from .routes.scan_routes import scan_bp
    from .routes.encode_routes import encode_bp
    
    app.register_blueprint(scan_bp, url_prefix='/api')
    app.register_blueprint(encode_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
