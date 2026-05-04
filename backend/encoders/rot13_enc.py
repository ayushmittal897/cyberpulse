import codecs

def encode(text: str) -> str:
    return codecs.encode(text, 'rot_13')

def decode(text: str) -> str:
    # ROT13 is its own inverse
    return codecs.encode(text, 'rot_13')
