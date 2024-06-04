function takeTurn() {
    const laborHours = document.getElementById('labor-hours').value;
    const researchHours = document.getElementById('research-hours').value;
    const leisureHours = document.getElementById('leisure-hours').value;

    fetch('http://localhost:5000/take-turn', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            labor_hours: laborHours,
            research_hours: researchHours,
            leisure_hours: leisureHours
        }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('game-state').innerHTML = `
            <p>Time: ${data.time}</p>
            <p>Dollars: ${data.dollars}</p>
            <p>Psyche: ${data.psyche}</p>
            <p>Status: ${data.status}</p>
            <p>Portfolio: ${JSON.stringify(data.portfolio)}</p>
        `;
    })
    .catch(error => console.error('Error:', error));
}
