class Block:

	def __init__(self, point, character, color):
		self.point = point
		self.char = character
		self.color = color


class Piece:

	# Mike: "central" point from which others extend.
	# Mike: thus when you move down it just shifts central point
	# Mike: and when you rotate you merely shift orientation around central point.
	# Mike: The also allows for easy creation of different pieces as you just have to make the points.
	def __init__(self, points, pivot, character, color):
		self.pivot = pivot 
		#self.points = (block,block,block...)

	def move(self, base, direction):
		if direction = #keystroke down and pivot(1) + 1 != floor.location:
			self.pivot(1) = pivot(1) + 1
		elif direction = #keystroke down and pivot (1) + 1 = floor.location:
			self.hit = true #boolean to test if this piece has already hit the base once (will be absorbed during second hit)
			#run method from floor class to absorb this piece
		elif direction = #keystroke right and pivot(2) + 1 != floor.location:
			self.pivot(2) = pivot(2) + 1
		elif direction = #keystroke right and pivot(2) + 1 = floor.location:
			break #if it is rotating into base, it doesn't rotate.
		elif direction = #keystroke left and pivot(1) + 1 != floor.location:
			self.pivot(2) = pivot(2) - 1
		elif direction = #keystroke left and pivot(1) + 1 != floor.location:
			break #if it is rotating into base, it doesn't rotate.
			

	def rotate(self):
		for point in self.points
			self.point = point + 1


# Jono: Mike - I liked your use of 'floor' instead of 'base'.
class Floor:

	def __init__(self):
		pass

	def delete_rows(self):
		pass

	def add_piece(self, piece):
		pass

	def is_piece_hit(self, piece):
		pass

	def is_game_over(self):
		pass
