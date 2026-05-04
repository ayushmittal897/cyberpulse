import json
import os

def load_payloads():
    # Load payloads from frontend/assets/payloads.json
    base_dir = os.path.dirname(__file__)
    payloads_path = os.path.abspath(os.path.join(base_dir, '../../frontend/assets/payloads.json'))
    
    try:
        with open(payloads_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading payloads: {e}")
        return {"xss": [], "sqli": []}
