import random

class food:
	def __init__(self):
		self.foodx = 0
		self.foody = 0

	def get_food_pos(self,dis_width,dis_height,snake_block):
		self.foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
		self.foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
