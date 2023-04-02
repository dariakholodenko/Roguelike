import numpy as np
from typing import Optional
from tcod.console import Console

import tile_types
from entity import Entity

class GameMap:
	
	def __init__(self, width: int, height: int, entities: list[Entity]):
		self.width = width
		self.height = height
		self.tiles = np.full(shape=(width, height), fill_value=tile_types.WALL, order='C') # order 'C' = row-wise
		self.entities = entities
	
	def add_entity(self, entity: Entity):
		self.entities.append(entity)
			
		
	def update_render_order(self):
		self.entities.sort(key=Entity.render_priority)		
	
	def if_actor_entity_at(self, x: int, y: int) -> Optional[Entity]:
		for entity in self.entities:
			if entity.position == (x,y) and entity.walkable == False:
				return entity
			
		return None
	
	#def order_rendering(self, entities: list[Entity]):
		
				
	def render(self, console: Console)-> None:
		for row, col in np.ndindex(self.tiles.shape):
			tile = self.tiles[row][col]
			console.print(x=row, y=col, string=tile.char, fg=tile.color, bg=tile.bg)
		
		for entity in self.entities:
			console.print(x=entity.x, y=entity.y, string=entity.char, fg=entity.color)
			
			
			
		

		
