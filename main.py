import eel
from game_loop import GameLoop

game = GameLoop()

eel.init('web')

@eel.expose
def process_turn(labor_hours, research_hours, leisure_hours):
    game.process_turn(labor_hours, research_hours, leisure_hours)
    return game.get_game_state()

eel.start('index.html', size=(800, 600))
