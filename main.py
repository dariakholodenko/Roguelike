#!/usr/bin/env python3
import tcod

from actions import Action, ExitAction, MovementAction
from input_handler import EventHandler
from engine import Engine
from map_generation import generate_map
from entity_factory import entity_factory


def main() -> None:
	screen_width = 100
	screen_height = 60
	
	min_rooms = 10
	max_rooms = 15
	min_room_size = 10 #minimum for width and height of rooms
	max_room_size = 12 #maximum for width and height of rooms
	
	#Initializing tileset via library predefined file
	tileset = tcod.tileset.load_tilesheet(
		"dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
	)
	
	player = entity_factory("player")
	
	game_map = generate_map(
		screen_width, 
		screen_height,
		min_rooms,
		max_rooms,
		min_room_size,
		max_room_size,
		player
	)
	

	#Defining an engine which is responsible for handling user's actions 
	#and render map and entities
	engine = Engine(game_map, EventHandler(), player)
	
	with tcod.context.new_terminal(
		columns=screen_width,
		rows=screen_height,
		#loading the font for the context
		tileset=tileset, 
		#synchronizes game frame refresh rate with monitor's
		vsync=True, 
		title="Yet Another Roguelike"
	) as context:
		#creates a console
		main_console = tcod.Console(screen_width, screen_height, order="F")
		while True:
			engine.render(main_console, context)
			engine.handle_events(tcod.event.wait())	
	
if __name__ == "__main__":
    main()
