from typing import Optional
from entity import *
from game_map import GameMap

class Action:
	def perform(self):
		pass
	
class ExitAction(Action):
	def __init__(self):
		super().__init__()
	
	def perform(self):
		raise SystemExit()
	
class MovementAction(Action):
	def __init__(self, dx: int, dy: int):
		super().__init__()
		
		self.dx = dx
		self.dy = dy
	
	def perform(self, entity: Entity):
		entity.move(self.dx, self.dy)
		
class AttackAction(Action):
	def __init__(self):
		super().__init__()
			
	def perform(self, player: Entity, entity: Entity, game_map: GameMap):
		"""both attack and damage occur"""
		player.attack(entity)
		
		if(entity.is_alive == False): 
			game_map.kill_entity(entity)

class DirectionAction(Action):
	def __init__(self, dx: int, dy: int):
		super().__init__()
		
		self.dx = dx
		self.dy = dy
	
	def perform(self, player: Entity, game_map: GameMap) -> Optional[Action]:
		if player.is_alive == True:
			(dest_x, dest_y) = (player.x + self.dx, player.y + self.dy)
			
			entity = game_map.if_entity_at(dest_x, dest_y)
			
			if isinstance(entity, Actor) and entity.is_alive == True:
				return AttackAction().perform(player, entity, game_map)
			
			if isinstance(entity, Potion):
				return PickupAction().perform(player, entity, game_map)
			
			elif game_map.tiles[dest_x][dest_y].walkable:
					return MovementAction(self.dx, self.dy).perform(player)
		
		else: 
			return

class PickupAction(Action):
	def __init__(self):
		super().__init__()
	
	def perform(self, player: Entity, entity: Entity, game_map: GameMap):
		player.add_to_inventory(entity)
		game_map.remove_entity(entity)

class OpenInventoryAction(Action):
	def perform(self, player: Entity, game_map: GameMap = None):
		print("Inventory opened")
