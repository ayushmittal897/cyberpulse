import urllib.parse
from backend.utils.http_client import get_session
from backend.utils.payload_store import load_payloads

def check_xss(url):
    payloads = load_payloads().get("xss", [])
    session = get_session()
    
    # We will test a simple parameter injection, e.g. appending ?q=<payload>
    # In a real scanner, we'd parse forms and parameters.
    for payload in payloads:
        try:
            target_url = url + ("&" if "?" in url else "?") + "q=" + urllib.parse.quote(payload)
            response = session.get(target_url, verify=False, timeout=5)
            if payload in response.text:
                return {
                    "type": "XSS",
                    "status": "Vulnerable",
                    "severity": "Critical",
                    "color": "red",
                    "details": f"Reflected XSS found with payload: {payload}"
                }
        except Exception:
            pass

    return {
        "type": "XSS",
        "status": "Safe",
        "severity": "Safe",
        "color": "green",
        "details": "No generic reflected XSS detected."
    }
