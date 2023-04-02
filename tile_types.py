import numpy as np 

import colors

class Tile:
	
	def __init__(
		self, 
		walkable: bool, 
		char: str, 
		color: tuple[int,int,int], 
		bg: tuple[int,int,int] = colors.BLACK
	):
		self.walkable = walkable
		self.char = char
		self.color = color
		self.bg = bg

FLOOR = Tile(walkable=True, char=".", color=colors.BLUE, bg = colors.BLACK)
WALL = Tile(walkable=False, char="#", color=colors.SWAMP, bg = colors.BLACK)
VOID = Tile(walkable=False, char="", color=colors.BLACK, bg = colors.BLACK)
