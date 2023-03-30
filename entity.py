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
		name: str
	): #x: int = 0, y: int = 0, char: str = "?", color: tuple[int,int,int] = (0,255,100)): 
		
		self.x = x
		self.y = y
		self.char = char
		self.color = color
		self.name = name
		self.walkable = False
	
	@property
	def position(self) -> tuple[int, int]:
		return (self.x, self.y)
	
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
	): #x: int = 0, y: int = 0, 
		
		super().__init__(x, y, char, color, name)
		self.hp = hp
		self.damage = damage
		self.defense = defense
		self.dead = False
		self.attacking = True
		
	def kill_entity(self) -> None:
		print(self.char, " has been killed")
		self.dead = True
		self.char = "%"
		self.color = colors.RED
		self.walkable = True
		self.attacking = False
		
	def take_damage(self, other) -> None: 
		if self.dead == True or other.dead == True:
			return
		
		if self.defense >= other.damage:
			damage_factor = 0
		else:
			damage_factor = other.damage - self.defense
			
		self.hp -= damage_factor
		
		#if hp <= 0 turn the entity to dead
		if self.hp <= 0:
			self.kill_entity()
		
		
