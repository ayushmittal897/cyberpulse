from flask import Blueprint, request, jsonify
from backend.encoders import base64_enc, url_enc, html_enc, jwt_enc, hex_enc, binary_enc, rot13_enc, hash_enc

encode_bp = Blueprint('encode_routes', __name__)

@encode_bp.route('/encode', methods=['POST'])
def encode():
    data = request.get_json()
    codec = data.get('codec')
    text = data.get('text')
    
    if not text or not codec:
        return jsonify({"error": "Missing codec or text"}), 400

    try:
        if codec == 'base64':
            res = base64_enc.encode(text)
        elif codec == 'url':
            res = url_enc.encode(text)
        elif codec == 'html':
            res = html_enc.encode(text)
        elif codec == 'hex':
            res = hex_enc.encode(text)
        elif codec == 'binary':
            res = binary_enc.encode(text)
        elif codec == 'rot13':
            res = rot13_enc.encode(text)
        elif codec == 'sha256':
            res = hash_enc.encode(text, 'sha256')
        elif codec == 'md5':
            res = hash_enc.encode(text, 'md5')
        elif codec == 'sha512':
            res = hash_enc.encode(text, 'sha512')
        else:
            return jsonify({"error": "Unsupported codec for encoding"}), 400
        return jsonify({"result": res})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@encode_bp.route('/decode', methods=['POST'])
def decode():
    data = request.get_json()
    codec = data.get('codec')
    text = data.get('text')
    
    if not text or not codec:
        return jsonify({"error": "Missing codec or text"}), 400

    try:
        if codec == 'base64':
            res = base64_enc.decode(text)
        elif codec == 'url':
            res = url_enc.decode(text)
        elif codec == 'html':
            res = html_enc.decode(text)
        elif codec == 'jwt':
            res = jwt_enc.decode(text)
        elif codec == 'hex':
            res = hex_enc.decode(text)
        elif codec == 'binary':
            res = binary_enc.decode(text)
        elif codec == 'rot13':
            res = rot13_enc.decode(text)
        elif codec in ['sha256', 'md5', 'sha512']:
            return jsonify({"error": "Hashes cannot be decoded."}), 400
        else:
            return jsonify({"error": "Unsupported codec for decoding"}), 400
        return jsonify({"result": res})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
