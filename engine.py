from typing import Iterable, Any

from tcod.console import Console
from tcod.context import Context

from input_handler import EventHandler
from entity import Entity
from actions import ExitAction, MovementAction, DirectionAction
from gui import render_health_bar
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

			if isinstance(action, ExitAction):
				action.perform()
				
			else: action.perform(self.player, self.game_map)
					
	def render(self, console: Console, context: Context) -> None:
		self.game_map.render(console)
		
		render_health_bar(console, 20, self.player.warrior.max_hp, self.player.warrior.hp)
		context.present(console)
		console.clear()
