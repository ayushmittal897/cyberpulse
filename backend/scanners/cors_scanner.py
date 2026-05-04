from backend.utils.http_client import get_session

def check_cors(url):
    session = get_session()
    evil_origin = "https://evil-attacker.com"
    
    try:
        # Send a request with a fake Origin header
        headers = {'Origin': evil_origin}
        response = session.get(url, headers=headers, verify=False, timeout=5)
        
        acao = response.headers.get('Access-Control-Allow-Origin', '')
        acac = response.headers.get('Access-Control-Allow-Credentials', '')
        
        if acao == evil_origin or acao == '*':
            severity = "Critical" if (acac.lower() == 'true') else "Warning"
            color = "red" if severity == "Critical" else "yellow"
            
            return {
                "type": "CORS Policy",
                "status": "Vulnerable",
                "severity": severity,
                "color": color,
                "details": f"CORS Misconfiguration! ACAO reflects origin ('{acao}'). Credentials allowed: {acac}"
            }
            
        return {
            "type": "CORS Policy",
            "status": "Safe",
            "severity": "Safe",
            "color": "green",
            "details": "CORS policy appears secure or is not implemented."
        }
        
    except Exception as e:
        return {
            "type": "CORS Policy",
            "status": "Error",
            "severity": "Warning",
            "color": "yellow",
            "details": "Failed to check CORS headers."
        }
