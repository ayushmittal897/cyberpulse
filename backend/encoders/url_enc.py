import urllib.parse

def encode(text: str) -> str:
    return urllib.parse.quote(text)

def decode(text: str) -> str:
    return urllib.parse.unquote(text)
