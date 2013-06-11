class Block:

	def __init__(self, point, character, color):
		self.point = point
		self.char = character
		self.color = color


class Piece:

	# TODO: absolute points or based on pivot?
	def __init__(self, points, pivot, character, color):
		pass

	def move_down():
		pass

	def rotate():
		pass

	# TODO: combine the 'move_down' and 'move_side' methods perhaps?
	def move_side(base, direction):
		pass

