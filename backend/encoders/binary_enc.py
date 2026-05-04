def encode(text: str) -> str:
    return ' '.join(format(ord(c), '08b') for c in text)

def decode(text: str) -> str:
    try:
        # Support both spaced and unspaced binary strings
        if " " not in text and len(text) % 8 == 0:
            binary_values = [text[i:i+8] for i in range(0, len(text), 8)]
        else:
            binary_values = text.split()
        return ''.join(chr(int(b, 2)) for b in binary_values)
    except Exception as e:
        raise ValueError(f"Invalid binary string: {str(e)}")
