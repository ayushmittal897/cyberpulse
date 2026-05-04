import hashlib

def encode(text: str, algo: str) -> str:
    if algo == 'sha256':
        return hashlib.sha256(text.encode('utf-8')).hexdigest()
    elif algo == 'md5':
        return hashlib.md5(text.encode('utf-8')).hexdigest()
    elif algo == 'sha512':
        return hashlib.sha512(text.encode('utf-8')).hexdigest()
    raise ValueError("Unsupported hashing algorithm")
