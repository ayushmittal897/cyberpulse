import ssl
import socket
from urllib.parse import urlparse
import datetime

def check_ssl(url):
    parsed = urlparse(url)
    hostname = parsed.hostname
    if not hostname:
        return {
            "type": "SSL",
            "status": "Error",
            "severity": "Warning",
            "color": "yellow",
            "details": "Invalid URL or no hostname."
        }
        
    if parsed.scheme != 'https':
        return {
            "type": "SSL",
            "status": "Vulnerable",
            "severity": "Critical",
            "color": "red",
            "details": "Connection is not using HTTPS."
        }

    port = parsed.port or 443
    context = ssl.create_default_context()
    
    try:
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                # Check expiration
                not_after = cert.get('notAfter')
                if not_after:
                    expire_date = datetime.datetime.strptime(not_after, '%b %d %H:%M:%S %Y %Z')
                    if datetime.datetime.utcnow() > expire_date:
                        return {
                            "type": "SSL",
                            "status": "Vulnerable",
                            "severity": "Critical",
                            "color": "red",
                            "details": "SSL Certificate has expired."
                        }
                        
                return {
                    "type": "SSL",
                    "status": "Safe",
                    "severity": "Safe",
                    "color": "green",
                    "details": "SSL Certificate is valid and active."
                }
    except Exception as e:
        return {
            "type": "SSL",
            "status": "Warning",
            "severity": "Warning",
            "color": "yellow",
            "details": f"SSL connection failed: {str(e)}"
        }
