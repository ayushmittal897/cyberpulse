# CyberPulse

Visually immersive web-based cybersecurity tool.
Stack: Python · Flask · Flask-SocketIO · Vanilla JS · HTML5 · CSS3

## Features
- Real-time vulnerability scanning via Socket.io
- SSL, XSS, SQLi, and Security Headers detection
- Data encoding/decoding suite (Base64, URL, HTML, JWT)
- Terminal UI with live logging

## Setup
1. Create virtual environment
```bash
python -m venv venv
```
2. Activate virtual environment
```bash
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Environment variables
Create a `.env` file based on `.env.example` (or use the one provided).

5. Run
```bash
python run.py
```

## Structure
- `backend/` - Flask API and security scanners
- `frontend/` - Static assets, HTML, CSS, JS
- `run.py` - Application entry point
