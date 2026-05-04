function startRadar() {
    const radar = document.getElementById('radar');
    radar.classList.add('active');
}

function stopRadar() {
    const radar = document.getElementById('radar');
    radar.classList.remove('active');
}

function addBlip(color) {
    const radar = document.getElementById('radar');
    if (!radar.classList.contains('active')) return;
    
    const blip = document.createElement('div');
    blip.className = `blip ${color}`;
    
    // Radar center is 100, 100 (since width/height is 200px)
    const angle = Math.random() * Math.PI * 2;
    const radius = Math.random() * 85; // keep it slightly inside the edge
    
    const x = 100 + radius * Math.cos(angle);
    const y = 100 + radius * Math.sin(angle);
    
    blip.style.left = `${x}px`;
    blip.style.top = `${y}px`;
    
    radar.appendChild(blip);
    
    // Remove after animation completes (4s)
    setTimeout(() => {
        blip.remove();
    }, 4000);
}
