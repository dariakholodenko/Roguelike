from entity import Entity
from game_map import GameMap

class Action:
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
	def __init__(self, dx: int, dy: int):
		super().__init__()
		
		self.dx = dx
		self.dy = dy
	
	def perform(self, entity1: Entity, entity2: Entity, game_map: GameMap):
		entity1.take_damage(entity2)
		entity2.take_damage(entity1)
		
		if(entity1.isAlive == False or entity2.isAlive == False):
			game_map.update_render_order()

class DirectionAction(Action):
	def __init__(self, dx: int, dy: int):
		super().__init__()
		
		self.dx = dx
		self.dy = dy
	
	def perform(self, entity1: Entity, entity2: Entity = None, game_map: GameMap = None):
		if isinstance(entity2, Entity):
			return AttackAction(self.dx, self.dy).perform(
														entity1, 
														entity2, 
														game_map
													)
		
		else:
			return MovementAction(self.dx, self.dy).perform(entity1)
