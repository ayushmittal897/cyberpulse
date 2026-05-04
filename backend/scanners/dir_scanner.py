from backend.utils.http_client import get_session
import time

def check_directories(url, socketio=None):
    session = get_session()
    
    # Common sensitive files and directories
    payloads = [
        '.env', '.git/config', 'admin/', 'login/', 'backup.zip', 
        'wp-config.php', 'api/v1/', 'robots.txt', 'server-status'
    ]
    
    base_url = url if url.endswith('/') else url + '/'
    found_paths = []
    
    for path in payloads:
        target_url = base_url + path
        if socketio:
            socketio.emit('scan_log', {'message': f'DIR: Testing {target_url}...'})
        
        try:
            # We don't want to follow redirects for directory brute forcing usually,
            # but for a simple tool, a 200 OK is enough.
            response = session.get(target_url, verify=False, timeout=3, allow_redirects=False)
            
            # If 200 OK, it exists!
            if response.status_code == 200:
                found_paths.append(f"/{path} (200 OK)")
                if socketio:
                    socketio.emit('scan_log', {'message': f'[+] FOUND: /{path}'})
            elif response.status_code in [301, 302, 307, 308]:
                found_paths.append(f"/{path} ({response.status_code} Redirect)")
                if socketio:
                    socketio.emit('scan_log', {'message': f'[-] REDIRECT: /{path}'})
            elif response.status_code == 403:
                found_paths.append(f"/{path} (403 Forbidden)")
                if socketio:
                    socketio.emit('scan_log', {'message': f'[-] FORBIDDEN: /{path}'})
        except Exception:
            pass
        
        # Small delay to simulate real tool and not overwhelm the server
        time.sleep(0.2)

    if any("200 OK" in p for p in found_paths):
        return {
            "type": "Directory Brute-Force",
            "status": "Vulnerable",
            "severity": "Warning",
            "color": "yellow",
            "details": f"Sensitive paths found: {', '.join(found_paths)}"
        }
    elif found_paths:
         return {
            "type": "Directory Brute-Force",
            "status": "Info",
            "severity": "Safe",
            "color": "green",
            "details": f"Paths found (Redirects/Forbidden): {', '.join(found_paths)}"
        }
    else:
        return {
            "type": "Directory Brute-Force",
            "status": "Safe",
            "severity": "Safe",
            "color": "green",
            "details": "No common sensitive directories found."
        }
