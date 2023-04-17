
class Inventory:
	def __init__(self, capacity: int):
		self.capacity = capacity
		self.items: list = []
	
	def put(self, item) -> None:
		if len(self.items) < self.capacity:
			self.items.append(item)
			print(f'{item.name} has been added')
	
	def pick(self, item) -> None:
		self.items.remove(item)
		self.capacity -= 1
		print(f'{item.name} has been removed')

