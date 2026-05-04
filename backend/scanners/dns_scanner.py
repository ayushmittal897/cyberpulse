import socket
from urllib.parse import urlparse

def check_dns(url):
    parsed = urlparse(url)
    hostname = parsed.hostname
    if not hostname:
        return {
            "type": "DNS Recon",
            "status": "Error",
            "severity": "Warning",
            "color": "yellow",
            "details": "Invalid URL or no hostname."
        }

    try:
        ip_addr = socket.gethostbyname(hostname)
        aliases = []
        try:
            name, aliaslist, addresslist = socket.gethostbyaddr(ip_addr)
            if name != hostname:
                aliases.append(name)
            aliases.extend(aliaslist)
        except Exception:
            pass
            
        details = f"Resolved IP: {ip_addr}"
        if aliases:
            details += f" | Aliases: {', '.join(aliases)}"
            
        return {
            "type": "DNS Recon",
            "status": "Info",
            "severity": "Safe",
            "color": "green",
            "details": details
        }
    except Exception as e:
        return {
            "type": "DNS Recon",
            "status": "Error",
            "severity": "Warning",
            "color": "yellow",
            "details": f"Failed to resolve DNS: {str(e)}"
        }
