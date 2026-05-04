from backend.utils.http_client import get_session

def check_headers(url):
    session = get_session()
    missing_headers = []
    
    try:
        response = session.get(url, verify=False, timeout=5)
        headers = response.headers
        
        security_headers = [
            'Strict-Transport-Security',
            'Content-Security-Policy',
            'X-Frame-Options',
            'X-Content-Type-Options'
        ]
        
        for h in security_headers:
            if h not in headers:
                missing_headers.append(h)
                
        if missing_headers:
            return {
                "type": "Security Headers",
                "status": "Warning",
                "severity": "Warning",
                "color": "yellow",
                "details": f"Missing headers: {', '.join(missing_headers)}"
            }
        else:
            return {
                "type": "Security Headers",
                "status": "Safe",
                "severity": "Safe",
                "color": "green",
                "details": "All essential security headers are present."
            }
            
    except Exception as e:
        return {
            "type": "Security Headers",
            "status": "Error",
            "severity": "Warning",
            "color": "yellow",
            "details": "Could not fetch headers."
        }
