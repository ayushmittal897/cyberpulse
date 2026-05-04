document.getElementById('encode-btn').addEventListener('click', async () => {
    await processCodec('/api/encode');
});

document.getElementById('decode-btn').addEventListener('click', async () => {
    await processCodec('/api/decode');
});

async function processCodec(endpoint) {
    const codec = document.getElementById('codec-select').value;
    const text = document.getElementById('encoder-input').value;
    const outputArea = document.getElementById('encoder-output');
    
    if (!text) return;

    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ codec, text })
        });
        
        const data = await response.json();
        if (data.error) {
            outputArea.value = `Error: ${data.error}`;
        } else {
            outputArea.value = data.result;
        }
    } catch (err) {
        outputArea.value = `Error: ${err.message}`;
    }
}

document.getElementById('encoder-export-txt').addEventListener('click', () => {
    const outputText = document.getElementById('encoder-output').value;
    if (!outputText) return;
    
    const dataStr = "data:text/plain;charset=utf-8," + encodeURIComponent(outputText);
    downloadFile(dataStr, "cyberpulse_encoder_output.txt");
});

document.getElementById('encoder-export-json').addEventListener('click', () => {
    const outputText = document.getElementById('encoder-output').value;
    const inputText = document.getElementById('encoder-input').value;
    const codec = document.getElementById('codec-select').value;
    if (!outputText) return;
    
    const report = {
        timestamp: new Date().toISOString(),
        codec: codec,
        input: inputText,
        output: outputText
    };
    
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(report, null, 2));
    downloadFile(dataStr, "cyberpulse_encoder_output.json");
});

function downloadFile(dataUrl, filename) {
    const downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href", dataUrl);
    downloadAnchorNode.setAttribute("download", filename);
    document.body.appendChild(downloadAnchorNode);
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
}
