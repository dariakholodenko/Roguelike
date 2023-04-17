from copy import deepcopy
from entity import *
import colors
from warrior import Warrior
from inventory import Inventory

entities_types = {
		"player": Actor(
				char = "@", 
				color = colors.WHITE, 
				name = "player", 
				warrior = Warrior(
					max_hp = 50, 
					base_damage = 1, 
					base_defense = 1
				),
				inventory = Inventory(capacity = 10)
				
			),
		
		"corpse": Entity(
				char = "%", 
				color = colors.RED, 
				name = "corpse",
				render_priority = -1
			),
			
		"goblin": Actor(
				char = "g", 
				color = colors.GREEN, 
				name = "goblin", 
				warrior = Warrior(
					max_hp = 5, 
					base_damage = 2, 
					base_defense = 0
				),
				inventory = Inventory(capacity = 0)
			),
			
		"healing potion": Potion(
				char = "*",
				color = colors.DEEP_PINK,
				name = "healing potion",
				restoration = 5
			),	
		
		
	}
	
def entity_factory(name: str):
	if name in entities_types.keys():
		new_entity = deepcopy(entities_types[name])
		return new_entity
		
	return Actor()
