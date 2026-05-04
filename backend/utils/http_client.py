import requests
from config import Config

def get_session():
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'CyberPulse-Security-Scanner/1.0'
    })
    return session

def fetch(url, timeout=None):
    if timeout is None:
        timeout = Config.SCAN_TIMEOUT
    session = get_session()
    try:
        response = session.get(url, timeout=timeout, verify=False, allow_redirects=True)
        return response
    except requests.RequestException as e:
        return None
