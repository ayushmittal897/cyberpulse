from flask import Blueprint, request, jsonify
from backend.app import socketio
from backend.scanners.xss_scanner import check_xss
from backend.scanners.sqli_scanner import check_sqli
from backend.scanners.header_scanner import check_headers
from backend.scanners.ssl_scanner import check_ssl
from backend.scanners.nmap_scanner import check_nmap
from backend.scanners.dir_scanner import check_directories
from backend.scanners.cors_scanner import check_cors
from backend.scanners.cookie_scanner import check_cookies
from backend.scanners.dns_scanner import check_dns

scan_bp = Blueprint('scan_routes', __name__)

@scan_bp.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    socketio.emit('scan_log', {'message': f'Starting scan for {url}'})
    
    results = []
    
    # DNS Recon
    dns_res = check_dns(url)
    results.append(dns_res)
    socketio.emit('scan_log', {'message': f'DNS Recon: {dns_res["status"]} - {dns_res.get("details", "")}'})
    
    # SSL Check
    ssl_res = check_ssl(url)
    results.append(ssl_res)
    socketio.emit('scan_log', {'message': f'SSL Scan: {ssl_res["status"]} - {ssl_res.get("details", "")}'})

    # Headers Check
    headers_res = check_headers(url)
    results.append(headers_res)
    socketio.emit('scan_log', {'message': f'Header Scan completed.'})

    # XSS Check
    xss_res = check_xss(url)
    results.append(xss_res)
    socketio.emit('scan_log', {'message': f'XSS Scan completed.'})

    # SQLi Check
    sqli_res = check_sqli(url)
    results.append(sqli_res)
    socketio.emit('scan_log', {'message': f'SQLi Scan completed.'})

    # CORS Check
    cors_res = check_cors(url)
    results.append(cors_res)
    socketio.emit('scan_log', {'message': f'CORS Scan completed.'})

    # Cookie Check
    cookie_res = check_cookies(url)
    results.append(cookie_res)
    socketio.emit('scan_log', {'message': f'Cookie Security Scan completed.'})

    # Dirbuster Check
    socketio.emit('scan_log', {'message': f'Starting Directory Brute-Force...'})
    dir_res = check_directories(url, socketio)
    results.append(dir_res)
    socketio.emit('scan_log', {'message': f'Directory Brute-Force completed.'})

    # Nmap Check
    socketio.emit('scan_log', {'message': f'Starting Nmap Scan...'})
    nmap_res = check_nmap(url)
    results.append(nmap_res)
    socketio.emit('scan_log', {'message': f'Nmap Scan completed.'})

    socketio.emit('scan_log', {'message': f'Scan complete.'})
    
    return jsonify({"results": results})
