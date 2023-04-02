import colors 

class Entity:
	"""
	Generic entity class
	"""
	def __init__(
		self, 
		x: int, 
		y: int, 
		char: str, 
		color: tuple[int,int,int], 
		name: str,
		render_priority: int = 0
	):
		
		self.x = x
		self.y = y
		self.char = char
		self.color = color
		self.name = name
		self.walkable = False
		self.render_priority = render_priority
	
	@property
	def position(self) -> tuple[int, int]:
		return (self.x, self.y)
		
	#@property
	def render_priority(self) -> int:
		return self.render_priority
	
	@position.setter
	def position(self, pos: tuple[int, int]):
		(self.x, self.y) = pos
	
	def move(self, dx: int, dy: int) -> None:
		self.x += dx
		self.y += dy

class Enemy(Entity):
	def __init__(
		self, 
		x: int = 0, 
		y: int = 0, 
		char: str = "?", 
		color: tuple[int,int,int] = (0,255,100), 
		name: str = "No name",
		hp: int = 5, 
		damage: int = 2, 
		defense: int = 0
	):
		
		super().__init__(x, y, char, color, name)
		self.hp = hp
		self.damage = damage
		self.defense = defense
		self.isAlive = True
		self.attacking = True
		
	def kill_entity(self) -> None:
		print(f'{self.name} has been killed')
		self.isAlive = False
		self.char = "%"
		self.color = colors.RED
		self.walkable = True
		self.attacking = False
		self.render_priority = -1
		
	def take_damage(self, other) -> None: 
		if self.isAlive == False or other.isAlive == False:
			return
		
		if self.defense >= other.damage:
			damage_factor = 0
		else:
			damage_factor = other.damage - self.defense
			
		self.hp -= damage_factor
		
		#if hp <= 0 turn the entity to dead
		if self.hp <= 0:
			self.kill_entity()
		
		
