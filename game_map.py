import numpy as np
from typing import Optional
from tcod.console import Console

from entity_factory import entity_factory
import tile_types
from entity import Entity

class GameMap:
	
	def __init__(self, width: int, height: int, entities: list[Entity]):
		self.width = width
		self.height = height
		self.tiles = np.full(shape=(width, height), fill_value=tile_types.WALL, order='C') # order 'C' = row-wise
		self.entities = entities
	
	def update_render_order(self) -> None:
		self.entities.sort(key=Entity.render_priority)	
		
	def add_entity(self, entity: Entity) -> None:
		self.entities.append(entity)
		self.update_render_order()	
		
	def remove_entity(self, entity: Entity) -> None:
		self.entities.remove(entity)
	
	def kill_entity(self, entity: Entity) -> None:
		print(f'{entity.name} has been killed')
		corpse = entity_factory("corpse")
		corpse.position = entity.position
		self.remove_entity(entity)
		self.add_entity(corpse)
	
	def if_entity_at(self, x: int, y: int) -> Optional[Entity]:
		for entity in self.entities:
			if entity.position == (x,y):
				return entity
			
		return None		
				
	def render(self, console: Console) -> None:
		for row, col in np.ndindex(self.tiles.shape):
			tile = self.tiles[row][col]
			console.print(x=row, y=col, string=tile.char, fg=tile.color, bg=tile.bg)
		
		for entity in self.entities:
			console.print(x=entity.x, y=entity.y, string=entity.char, fg=entity.color)
			
			
			
		

		
