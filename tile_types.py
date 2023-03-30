import numpy as np 

import colors

class Tile:
	
	def __init__(self, walkable: bool, char: str, color: tuple[int,int,int]):
		self.walkable = walkable
		self.char = char
		self.color = color

FLOOR = Tile(walkable=True, char=".", color=colors.BLUE)
WALL = Tile(walkable=False, char="#", color=colors.SWAMP)
		
