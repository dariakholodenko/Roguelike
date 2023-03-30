from entity import Entity, Enemy
import colors
#class EntityFactory:
#	def __init__(self, name: str):
#		entities_types = {
#			"player": Enemy("@", (255,255,255), 50, 1, 1)
#		}
#		
#		return entities_types[name]
entities_types = {
		"player": Enemy(char = "@", color = colors.WHITE, name = "player", hp = 50, damage = 1, defense = 1),
		
	}
	
def entity_factory(name: str):
	if name in entities_types.keys():
		return entities_types[name]
		
	return Enemy()
