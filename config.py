import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-dev-key')
    DEBUG = os.getenv('FLASK_DEBUG', 'True') == 'True'
    PORT = int(os.getenv('PORT', 5000))
    SCAN_TIMEOUT = int(os.getenv('SCAN_TIMEOUT', 10))
    CORS_ALLOWED_ORIGINS = "*"
