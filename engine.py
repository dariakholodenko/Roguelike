from typing import Iterable, Any

from tcod.console import Console
from tcod.context import Context

from input_handler import EventHandler
from entity import Entity, Enemy
from actions import ExitAction, MovementAction

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
					
				if isinstance(action, MovementAction):
					if self.player.dead == False:
						entity = self.game_map.if_actor_entity_at(self.player.x + action.dx, self.player.y + action.dy)
						
						if isinstance(entity, Enemy):
							"""To refactor:"""
							self.player.take_damage(entity)
							entity.take_damage(self.player)
							
						else:
							if self.game_map.tiles[self.player.x + action.dx][self.player.y + action.dy].walkable:
								self.player.move(dx = action.dx, dy = action.dy)	
				
				elif isinstance(action, ExitAction):
					raise SystemExit()
					
	def render(self, console: Console, context: Context) -> None:
		self.game_map.render(console)
			
		context.present(console)
		console.clear()
