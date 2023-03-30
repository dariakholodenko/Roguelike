import tcod.event

from actions import Action, ExitAction, MovementAction

MOVE_KEYS = {
	tcod.event.K_LEFT: (-1,0),
	tcod.event.K_RIGHT: (1,0),
	tcod.event.K_UP: (0,-1),
	tcod.event.K_DOWN: (0,1),
	
	#aswd
}

class EventHandler(tcod.event.EventDispatch[Action]):
	def ev_quit(self, event: tcod.event.Quit) -> None:
		action = ExitAction()
				
		return action
		
	def ev_keydown(self, event: tcod.event.KeyDown):
		key = event.sym
		if key in MOVE_KEYS:
			action = MovementAction(*MOVE_KEYS[key])
		else:
			action = None
		return action 
