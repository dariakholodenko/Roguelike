import numpy as np
from tcod.console import Console
from typing import Tuple
import tile_types
from entity import Entity

class GameMap:
	def __init__(self, width: int, height: int, entities: list[Entity]):
		self.width = width
		self.height = height
		self.tiles = np.full(shape=(width, height), fill_value=tile_types.WALL, order='C') # order 'C' = row-wise
		self.entities = entities
	
	def if_actor_entity_at(self, x: int, y: int) -> Entity: # or None
		for entity in self.entities:
			if entity.position == (x,y) and entity.walkable == False:
				return entity
			
		return None
				
	def render(self, console: Console)-> None:
		for row, col in np.ndindex(self.tiles.shape):
			tile = self.tiles[row][col]
			console.print(x=row, y=col, string=tile.char, fg=tile.color)
		
		for entity in self.entities:
			console.print(x=entity.x, y=entity.y, string=entity.char, fg=entity.color)
			
			
			
		

		
