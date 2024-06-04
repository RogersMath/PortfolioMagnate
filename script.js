function takeTurn() {
    const laborHours = parseInt(document.getElementById('labor-hours').value);
    const researchHours = parseInt(document.getElementById('research-hours').value);
    const leisureHours = parseInt(document.getElementById('leisure-hours').value);

    // Call the Python function to process the turn
    eel.process_turn(laborHours, researchHours, leisureHours)(function(game_state) {
        document.getElementById('game-state').innerHTML = `
            <p>Time: ${game_state.time}</p>
            <p>Dollars: ${game_state.dollars}</p>
            <p>Psyche: ${game_state.psyche}</p>
            <p>Status: ${game_state.status}</p>
            <p>Portfolio: ${JSON.stringify(game_state.portfolio)}</p>
        `;
    });
}
