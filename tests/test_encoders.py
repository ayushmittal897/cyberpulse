import pytest
from backend.encoders import base64_enc, url_enc, html_enc

def test_base64_encoder():
    original = "cyberpulse test"
    encoded = base64_enc.encode(original)
    decoded = base64_enc.decode(encoded)
    assert decoded == original

def test_url_encoder():
    original = "https://example.com/?q=test&id=1"
    encoded = url_enc.encode(original)
    decoded = url_enc.decode(encoded)
    assert decoded == original

def test_html_encoder():
    original = "<script>alert('xss')</script>"
    encoded = html_enc.encode(original)
    decoded = html_enc.decode(encoded)
    assert decoded == original
