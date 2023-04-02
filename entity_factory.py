from copy import deepcopy
from entity import Entity, Enemy
import colors

entities_types = {
		"player": Enemy(
				char = "@", 
				color = colors.WHITE, 
				name = "player", 
				hp = 50, 
				damage = 1, 
				defense = 1
			),
			
		"goblin": Enemy(
				char = "g", 
				color = colors.GREEN, 
				name = "goblin", 
				hp = 5, 
				damage = 2, 
				defense = 0
			),
		
		
		
	}
	
def entity_factory(name: str):
	if name in entities_types.keys():
		new_entity = deepcopy(entities_types[name])
		return new_entity
		
	return Enemy()
