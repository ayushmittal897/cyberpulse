from backend.utils.http_client import get_session

def check_cookies(url):
    session = get_session()
    
    try:
        response = session.get(url, verify=False, timeout=5)
        cookies = response.cookies
        
        if not cookies:
            return {
                "type": "Cookie Security",
                "status": "Safe",
                "severity": "Safe",
                "color": "green",
                "details": "No cookies are set by this endpoint."
            }
            
        insecure_cookies = []
        for cookie in cookies:
            issues = []
            if not cookie.secure:
                issues.append("Missing Secure flag")
            
            # response.cookies is a RequestsCookieJar, checking HttpOnly is a bit specific
            # we can check _rest for 'httponly'
            if not getattr(cookie, 'has_nonstandard_attr', lambda x: False)('HttpOnly') and 'httponly' not in str(cookie).lower():
                issues.append("Missing HttpOnly flag")
                
            if issues:
                insecure_cookies.append(f"{cookie.name} ({', '.join(issues)})")
                
        if insecure_cookies:
            return {
                "type": "Cookie Security",
                "status": "Warning",
                "severity": "Warning",
                "color": "yellow",
                "details": f"Insecure cookies found: {'; '.join(insecure_cookies)}"
            }
            
        return {
            "type": "Cookie Security",
            "status": "Safe",
            "severity": "Safe",
            "color": "green",
            "details": "All cookies appear to have Secure and HttpOnly flags."
        }
        
    except Exception as e:
        return {
            "type": "Cookie Security",
            "status": "Error",
            "severity": "Warning",
            "color": "yellow",
            "details": "Failed to retrieve cookies."
        }
