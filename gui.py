from tcod.console import Console

import colors

def render_health_bar(
		console: Console, 
		base_bar_width: int, 
		max_hp: int,
		current_hp: int
	) -> None:
	
	updated_width = int((current_hp/max_hp)*base_bar_width)
	
	console.draw_rect(x = 80, y = 1, width = base_bar_width, height = 1, ch = 1, bg = (102,0,0))#colors.RED)
	
	if updated_width > 0:
		console.draw_rect(x = 80, y = 1, width = updated_width, height = 1, ch = 1, bg = (0,102,51))#colors.GREEN)
	
	console.print(x = 81, y = 1, string = f"HP: {current_hp}/{max_hp}", fg = (245,245,245))#colors.WHITE)
