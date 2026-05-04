# Architecture

## Overview
CyberPulse uses a client-server architecture with Flask (Python) backend and a vanilla HTML/JS/CSS frontend. Real-time updates are handled via Flask-SocketIO.

## Components
1. **Frontend**: Serves as the UI shell. It communicates with the backend via REST endpoints for scans/encoders and listens to a Socket.io stream for real-time terminal logs.
2. **Backend/API**: Routes incoming requests. The scan pipeline executes multiple checks (SSL, XSS, SQLi, Headers) sequentially or concurrently, emitting logs via Socket.io.
3. **Scanners**: Modular vulnerability checks.
4. **Encoders**: Utility functions for data transformation.

## Real-time Data Flow
User initiates scan -> Frontend POSTs to `/api/scan` -> Flask executes scanners -> Scanners emit events -> Frontend Socket.io catches events and updates terminal UI -> Backend returns final JSON response -> Frontend updates visual UI.
