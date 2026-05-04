# API Reference

## 1. POST `/api/scan`
Initiates a vulnerability scan on the target URL.

**Request Body:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "results": [
    {
      "type": "SSL",
      "status": "Safe",
      "severity": "Safe",
      "color": "green",
      "details": "SSL Certificate is valid and active."
    }
  ]
}
```

## 2. POST `/api/encode`
Encodes text using the selected codec.

**Request Body:**
```json
{
  "codec": "base64",
  "text": "hello"
}
```

**Response:**
```json
{
  "result": "aGVsbG8="
}
```

## 3. POST `/api/decode`
Decodes text using the selected codec.
