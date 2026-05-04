import urllib.parse
from backend.utils.http_client import get_session
from backend.utils.payload_store import load_payloads

def check_sqli(url):
    payloads = load_payloads().get("sqli", [])
    session = get_session()
    
    sql_errors = ["syntax error", "mysql_fetch", "ora-", "postgresql", "sql syntax"]

    for payload in payloads:
        try:
            target_url = url + ("&" if "?" in url else "?") + "id=" + urllib.parse.quote(payload)
            response = session.get(target_url, verify=False, timeout=5)
            
            text_lower = response.text.lower()
            for err in sql_errors:
                if err in text_lower:
                    return {
                        "type": "SQLi",
                        "status": "Vulnerable",
                        "severity": "Critical",
                        "color": "red",
                        "details": f"SQL error detected with payload: {payload}"
                    }
        except Exception:
            pass

    return {
        "type": "SQLi",
        "status": "Safe",
        "severity": "Safe",
        "color": "green",
        "details": "No generic SQL injection detected."
    }
