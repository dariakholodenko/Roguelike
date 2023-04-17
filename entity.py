import colors 
from inventory import Inventory
from warrior import Warrior

"""
Base entity class
"""
class Entity:
	def __init__(
		self, 
		char: str, 
		color: tuple[int,int,int], 
		name: str,
		x: int = 0, 
		y: int = 0, 
		render_priority: int = 0
	):
		
		self.char = char
		self.color = color
		self.name = name
		self.x = x
		self.y = y
		self.render_priority = render_priority
		self.walkable = False
	
	@property
	def position(self) -> tuple[int, int]:
		return (self.x, self.y)
	
	@position.setter
	def position(self, pos: tuple[int, int]):
		(self.x, self.y) = pos
	
	def render_priority(self) -> int:
		return self.render_priority
		
	def move(self, dx: int, dy: int) -> None:
		self.x += dx
		self.y += dy

"""
Inherits a behavior of a genral entity 
and extended to actor entity by Composition 
"""
class Actor(Entity):
	def __init__(
		self, 
		*,
		char: str = "?", 
		color: tuple[int,int,int] = (0,255,100), 
		name: str = "Actor",
		x: int = 0, 
		y: int = 0,
		warrior: Warrior,
		inventory: Inventory
	):
		
		super().__init__(char, color, name, x, y)
		self.warrior = warrior
		self.inventory = inventory
		
	@property
	def is_alive(self) -> bool:
		return self.warrior.is_alive
	
	def attack(self, other) -> None:
		self.warrior.attack(other.warrior)
			
	def add_to_inventory(self, item):
		self.inventory.put(item)
		
class Potion(Entity):
	def __init__(
		self, 
		char: str = "!", 
		color: tuple[int,int,int] = (0,100,255), 
		name: str = "Potion",
		x: int = 0, 
		y: int = 0, 
		restoration: int = 0
	):
		
		super().__init__(char, color, name, x, y, render_priority = -1)
		self.restoration = restoration
		self.walkable = True
		
		@property
		def restoration(self):
			return self.restoration
