import pytest
from backend.scanners.header_scanner import check_headers
from backend.scanners.ssl_scanner import check_ssl

def test_header_scanner():
    # Example test pointing to a known domain
    # In a real scenario, mock the HTTP client
    result = check_headers("https://example.com")
    assert result["type"] == "Security Headers"
    assert result["status"] in ["Warning", "Safe"]

def test_ssl_scanner():
    result = check_ssl("https://example.com")
    assert result["type"] == "SSL"
    assert result["status"] in ["Safe", "Vulnerable", "Warning"]
