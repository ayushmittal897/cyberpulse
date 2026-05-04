const socket = io();
const terminalBody = document.getElementById('terminal-body');

socket.on('connect', () => {
    appendLog('System connected to backend socket.');
});

socket.on('scan_log', (data) => {
    appendLog(data.message);
    
    // Attempt to drop radar blips based on the message content
    if (typeof addBlip === 'function') {
        const msg = data.message.toLowerCase();
        if (msg.includes('error') || msg.includes('[-]')) {
            addBlip('red');
        } else if (msg.includes('warning') || msg.includes('redirect')) {
            addBlip('yellow');
        } else if (msg.includes('found') || msg.includes('safe') || msg.includes('[+]')) {
            addBlip('green');
        } else {
            // Normal scanning, drop random neutral/safe blips occasionally
            if (Math.random() > 0.4) {
                addBlip(Math.random() > 0.5 ? 'green' : 'yellow');
            }
        }
    }
});

function appendLog(message) {
    const div = document.createElement('div');
    div.className = 'log-entry';
    div.textContent = `> ${message}`;
    terminalBody.appendChild(div);
    terminalBody.scrollTop = terminalBody.scrollHeight;
}
