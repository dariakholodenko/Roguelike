import tcod
import random 
import numpy as np

from game_map import GameMap
import tile_types
from entity import Entity, Enemy
from entity_factory import entity_factory

"""Here's a map generation occures"""

class Room:
	def __init__(self, x_left: int, y_upper: int, width: int, height: int, idx: int):
		self.x_left, self.y_upper = x_left, y_upper
		self.width, self.height = width, height
		
		self.x_right = self.x_left + self.width
		self.y_lower = self.y_upper + self.height
		
		self.center_x = self.x_left + int(self.width/2)
		self.center_y = self.y_upper + int(self.height/2)
		
		self._idx = idx
	
	"""TEST ONLY"""
	@property
	def idx(self):
		return self._idx
		
	@property #center=Tuple[x, y] getter
	def center(self) -> tuple[int, int]:
		return (self.center_x, self.center_y)
		
	@property #size=Tuple[width, height] getter
	def size(self) -> tuple[int, int]:
		return (self.width, self.height)
	
	@property
	def inner(self) -> tuple[slice,slice]:
		return (
			slice(self.x_left+1, self.x_right-1), 
			slice(self.y_upper+1, self.y_lower-1)
		)
		
	def isintersects(self, other) -> bool:		
		result = (
			self.x_left <= other.x_right
			and self.x_right >= other.x_left
			and self.y_lower >= other.y_upper
			and self.y_upper <= other.y_lower
		)
		
		return result
			
			
def generate_rooms(
	map_width: int, 
	map_height: int, 
	min_rooms: int, 
	max_rooms: int, 
	min_room_size: int, 
	max_room_size: int
) -> list[Room]:
	
	rooms_number = random.randint(min_rooms, max_rooms)
	rooms = []
	
	#Try to generate a new room until there's no overlap with already created rooms
	i = 0
	while i < rooms_number:
		room_width = random.randint(min_room_size, max_room_size)
		room_height = random.randint(min_room_size, max_room_size)
		pos_x = random.randint(1, map_width-room_width-1)
		pos_y = random.randint(1, map_height-room_height-1)
		
		new_room = Room(pos_x, pos_y, room_width, room_height, i)
		
		if any(new_room.isintersects(other_room) for other_room in rooms):
			continue #there's an intersection so try again
		else: 
			rooms.append(new_room)
			i += 1

	return rooms

#Since by default all the map is a wall, turn the room's inner to floor
def add_room_to_map(tiles: np.ndarray, room: Room) -> None:
	tiles[room.inner] = tile_types.FLOOR
	
	"""TEST ONLY"""
	tiles[room.center] = tile_types.Tile(True, str(room.idx), (255,0,255))
	if room.idx >= 10:
		tiles[room.center[0]+1,room.center[1]] = tile_types.Tile(True, str(int(room.idx%10)), (255,0,255))
	
def make_tunnel(tiles: np.ndarray, room1: Room, room2: Room) -> None:
		if random.random() < 0.5:
			corner_x, corner_y = room2.center_x, room1.center_y #from above
		else:
			corner_x, corner_y = room1.center_x, room2.center_y #fron below
		
		for x, y in tcod.los.bresenham(room1.center, (corner_x, corner_y)).tolist():
			if tiles[x, y] == tile_types.WALL:
				tiles[x, y] = tile_types.FLOOR
			
		for x, y in tcod.los.bresenham((corner_x, corner_y), room2.center).tolist():
			if tiles[x, y] == tile_types.WALL:
				tiles[x, y] = tile_types.FLOOR

def place_player(room: Room, player: Entity) -> None:
	player.position = room.center
			
def generate_entities(game_map: GameMap, room: Room, entities: list[Entity]) -> None:
	enemies_num = random.randint(0,2)
	enemies_in_room = []
	i = 0
	
	while i < enemies_num:
		enemy_x = random.randint(room.x_left+2, room.x_right-2)
		enemy_y = random.randint(room.y_upper+2, room.y_lower-2)
		
		if any(entity.position == (enemy_x, enemy_y) for entity in enemies_in_room):
			continue
		else:
			new_enemy = entity_factory("goblin")
			new_enemy.position = (enemy_x, enemy_y)
			enemies_in_room.append(new_enemy)
			game_map.add_entity(new_enemy)
			i += 1
	
#Create a game map and add rooms in it
def generate_map(
	map_width: int, 
	map_height: int, 
	min_rooms: int,
	max_rooms: int,
	min_room_size: int,
	max_room_size: int,
	player: Entity
) -> GameMap:
	game_map = GameMap(map_width, map_height, entities = [player])
	
	rooms = generate_rooms(
		map_width, 
		map_height, 
		min_rooms, 
		max_rooms, 
		min_room_size, 
		max_room_size
	)
	
	for i in range(len(rooms)):
		if i == 0:
			place_player(rooms[i], player)
		else:
			generate_entities(game_map, rooms[i], game_map.entities)
			
		add_room_to_map(game_map.tiles, rooms[i])
		
		#connect each room with other two different ones
		j = random.choice([j for j in range(0, len(rooms)) if j != i])
		k = random.choice([k for k in range(0, len(rooms)) if k not in [i,j]])
		make_tunnel(game_map.tiles, rooms[i], rooms[j])
		make_tunnel(game_map.tiles, rooms[i], rooms[k])
	
	
	#return generated map and coordinates of a center of a first room to place a player
	return game_map
