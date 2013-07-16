class Block:

	def __init__(self, point, character, color):
		self.point = point
		self.char = character
		self.color = color


class Piece:

	# Constants for 'move' function.
	DOWN = 1
	RIGHT = 2
	LEFT = 3

	# Mike: "central" point from which others extend.
	# Mike: thus when you move down it just shifts central point
	# Mike: and when you rotate you merely shift orientation around central point.
	# Mike: The also allows for easy creation of different pieces as you just have to make the points.
	def __init__(self, points, pivot, character, color):
		self.pivot = pivot 
		#self.points = (block,block,block...)

	# Jono: returns a true/false value for whether or not the move was
	# Jono: successful (i.e., collision with floor)
	def move(self, floor, direction):
		# Store old pivot, in case movement hits the floor.
		old_pivot = self.pivot

		# Since there are possible many, many locations that would
		# need to be checked for floor collision, let's just move the
		# piece, then let the 'floor' object check it. If there is a
		# collision, we can just revert to the old pivot before we
		# redraw the game. (see below)
		if direction == DOWN:
			self.pivot(1) = pivot(1) + 1

		# continue if/else...
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

		# If we have a collision, revert to old pivot.
		if floor.is_piece_hit(self):
			self.pivot = old_pivot
			return False

		# If we made it here, the move was successful.
		return True

	def rotate(self):
		# TODO: matrix rotation

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
