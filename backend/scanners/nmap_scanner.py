import socket
from urllib.parse import urlparse
import concurrent.futures

def check_nmap(url):
    parsed = urlparse(url)
    hostname = parsed.hostname
    if not hostname:
        return {
            "type": "Port Scan (Nmap-style)",
            "status": "Error",
            "severity": "Warning",
            "color": "yellow",
            "details": "Invalid URL or no hostname."
        }

    # List of common ports to scan
    target_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 8080]
    open_ports = []
    vulnerable_services = []
    
    def scan_port(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1.0) # 1 second timeout
                result = s.connect_ex((hostname, port))
                if result == 0:
                    return port
        except:
            pass
        return None

    try:
        # Use ThreadPoolExecutor to scan ports concurrently
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(scan_port, target_ports)
            
            for port in results:
                if port is not None:
                    # Basic service identification by port number
                    service = "Unknown"
                    if port == 21: service = "FTP"
                    elif port == 22: service = "SSH"
                    elif port == 23: service = "Telnet"
                    elif port == 25: service = "SMTP"
                    elif port == 53: service = "DNS"
                    elif port == 80: service = "HTTP"
                    elif port == 110: service = "POP3"
                    elif port == 143: service = "IMAP"
                    elif port == 443: service = "HTTPS"
                    elif port == 3306: service = "MySQL"
                    elif port == 3389: service = "RDP"
                    elif port == 8080: service = "HTTP-Proxy"

                    port_info = f"Port {port} ({service})"
                    open_ports.append(port_info)
                    
                    # Highlight risky ports
                    if port in [21, 22, 23, 3306, 3389]:
                        vulnerable_services.append(port_info)

        if vulnerable_services:
            return {
                "type": "Port Scan (Nmap-style)",
                "status": "Vulnerable",
                "severity": "Critical",
                "color": "red",
                "details": f"Potentially vulnerable services: {', '.join(vulnerable_services)}. All open: {', '.join(open_ports)}"
            }
        elif open_ports:
            return {
                "type": "Port Scan (Nmap-style)",
                "status": "Warning",
                "severity": "Warning",
                "color": "yellow",
                "details": f"Open ports found: {', '.join(open_ports)}"
            }
        else:
            return {
                "type": "Port Scan (Nmap-style)",
                "status": "Safe",
                "severity": "Safe",
                "color": "green",
                "details": "No risky open ports detected."
            }

    except Exception as e:
         return {
            "type": "Port Scan (Nmap-style)",
            "status": "Error",
            "severity": "Warning",
            "color": "yellow",
            "details": f"Error during scan: {str(e)}"
        }
