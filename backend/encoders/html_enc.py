import html

def encode(text: str) -> str:
    return html.escape(text)

def decode(text: str) -> str:
    return html.unescape(text)
