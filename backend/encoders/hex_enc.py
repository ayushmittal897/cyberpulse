def encode(text: str) -> str:
    return text.encode('utf-8').hex()

def decode(text: str) -> str:
    try:
        # Ignore spaces and newlines
        clean_text = text.replace(" ", "").replace("\n", "")
        return bytes.fromhex(clean_text).decode('utf-8')
    except Exception as e:
        raise ValueError(f"Invalid hex string: {str(e)}")
