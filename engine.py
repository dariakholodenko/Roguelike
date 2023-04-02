from typing import Iterable, Any

from tcod.console import Console
from tcod.context import Context

from input_handler import EventHandler
from entity import Entity, Enemy
from actions import ExitAction, MovementAction, DirectionAction

from game_map import GameMap

"""
Engine handles events and renders entities

"""

class Engine:
	def __init__(self, game_map: GameMap, event_handler: EventHandler, player: Entity):
		self.game_map = game_map
		self.event_handler = event_handler
		self.player = player
		
	def handle_events(self, events: Iterable[Any]) -> None:
		for event in events:
			action = self.event_handler.dispatch(event)
			
			if action is None:
				continue
			
			"""To refactor:"""	
			if isinstance(action, DirectionAction):
				if self.player.isAlive == True:
					entity = self.game_map.if_actor_entity_at(
							self.player.x + action.dx, 
							self.player.y + action.dy
						)
					
					if isinstance(entity, Enemy):
						action.perform(self.player, entity, self.game_map)
						
					else:
						if self.game_map.tiles[self.player.x + action.dx][self.player.y + action.dy].walkable:
							action.perform(self.player)
			
			elif isinstance(action, ExitAction):
				action.perform()
					
	def render(self, console: Console, context: Context) -> None:
		self.game_map.render(console)
			
		context.present(console)
		console.clear()
