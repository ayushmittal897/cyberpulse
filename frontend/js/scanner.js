let currentScanResults = null;
let currentScanUrl = null;

document.getElementById('scan-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const url = document.getElementById('target-url').value;
    currentScanUrl = url;
    const resultsDiv = document.getElementById('scan-results');
    
    resultsDiv.innerHTML = '';
    startRadar();
    appendLog(`Initiating scan for: ${url}`);
    
    try {
        const response = await fetch('/api/scan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url })
        });
        
        const data = await response.json();
        if (data.error) {
            appendLog(`Error: ${data.error}`);
        } else {
            data.results.forEach(res => {
                const card = document.createElement('div');
                card.className = `result-card ${res.color}`;
                card.innerHTML = `
                    <div class="result-type">${res.type} [${res.status}]</div>
                    <div>${res.details}</div>
                `;
                resultsDiv.appendChild(card);
            });
            currentScanResults = data.results;
            document.getElementById('export-btn').style.display = 'block';
        }
    } catch (err) {
        appendLog(`Fetch error: ${err.message}`);
    } finally {
        stopRadar();
        appendLog(`Scan finished.`);
    }
});

document.getElementById('export-btn').addEventListener('click', () => {
    if (!currentScanResults) return;
    
    const report = {
        target: currentScanUrl,
        timestamp: new Date().toISOString(),
        results: currentScanResults
    };
    
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(report, null, 2));
    const downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href", dataStr);
    downloadAnchorNode.setAttribute("download", "cyberpulse_report.json");
    document.body.appendChild(downloadAnchorNode);
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
});
