import tcod.event
from typing import Optional

from actions import Action, ExitAction, MovementAction, DirectionAction, OpenInventoryAction

MOVE_KEYS = {
	tcod.event.K_LEFT: (-1,0),
	tcod.event.K_RIGHT: (1,0),
	tcod.event.K_UP: (0,-1),
	tcod.event.K_DOWN: (0,1)
}

PLAYER_DRIVEN_EVENTS_KEYS = {
	tcod.event.K_i: "Inventory"
}

class EventHandler(tcod.event.EventDispatch[Action]):
	def ev_quit(self, event: tcod.event.Quit) -> None:
		action = ExitAction()
				
		return action
		
	def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
		key = event.sym
		if key in MOVE_KEYS:
			action = DirectionAction(*MOVE_KEYS[key])
		elif key in PLAYER_DRIVEN_EVENTS_KEYS:
			action = OpenInventoryAction()
		else: action = None
		
		return action 
