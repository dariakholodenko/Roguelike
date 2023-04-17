class Warrior:
	def __init__(
		self,
		max_hp: int, 
		base_damage: int, 
		base_defense: int
	):
	
		self.max_hp = max_hp
		self.hp = max_hp
		self.base_damage = base_damage
		self.base_defense = base_defense
		self.is_alive = True
		self.attacking = True

#TO DO: add support for increased damage\defense with items	
	@property
	def damage(self):
		return self.base_damage
	
	@property
	def defense(self):
		return self.base_defense

	def turn_to_dead(self) -> None:
		self.is_alive = False
		#self.char = "%"
		#self.color = colors.RED
		self.walkable = True
		self.attacking = False
		#self.render_priority = -1
		
	def take_damage(self, other) -> None: 
		if self.attacking == False or other.attacking == False:
			return
		
		if self.defense >= other.damage:
			damage_factor = 0
		else:
			damage_factor = other.damage - self.defense
			
		self.hp -= damage_factor
		
		"""
		if hp <= 0 turn a composite entity to dead
		"""
		if self.hp <= 0:
			self.turn_to_dead()
		
	def attack(self, other) -> None:
		self.take_damage(other)
		other.take_damage(self)
