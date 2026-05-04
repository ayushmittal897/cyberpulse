import jwt
import json

def decode(token: str) -> str:
    try:
        # Decode without verification to just inspect claims
        decoded = jwt.decode(token, options={"verify_signature": False})
        return json.dumps(decoded, indent=2)
    except Exception as e:
        return f"Invalid JWT: {str(e)}"
