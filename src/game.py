class Block:

	def __init__(self, point, character, color):
		self.point = point
		self.char = character
		self.color = color


class Piece:

# Mike: TODO: arms... they are each a block so they need two locations.
			# They are fixed locations around the pivot.  We just don't
			# know which ones the random number generator will choose
			# So if it is this kind of piece rotate it this way.  elif this...
	# Constants for 'move' function.
	DOWN = 1
	RIGHT = 2
	LEFT = 3
	UP = 4

	# Mike: "central" point from which others extend.
	# Mike: thus when you move down it just shifts central point
	# Mike: and when you rotate you merely shift orientation around central point.
	# Mike: The also allows for easy creation of different pieces as you just have to make the points.
	def __init__(self, points, pivot, character, color):
		self.pivot = pivot 
		#self.points = (block,block,block...)

	# Jono: returns a true/false value for whether or not the move was
	# Jono: successful (i.e., collision with base)
	def move(self, base, direction):
	
		# Store old pivot, in case movement hits the base.
		old_pivot = self.pivot
		old_arms = self.arms

		if direction == DOWN:
			self.pivot(1) = pivot(1) + 1
		elif direction == LEFT:
			self.pivot(2) = pivot(2) - 1
		elif direction = RIGHT:
			self.pivot(2) = pivot(2) + 1
		elif direction = UP:
			self.rotate(self, base) #rotate to the right

		# If we have a collision, revert to old pivot.
		if self.hit(self, base) == 1:
			self.pivot = old_pivot
			self.arms = old_arms
			# Mike: pause?
			base.add_piece(base, self)
		elif self.hit(self, base) == 2:	
			self.pivot = old_pivot
			self.arms = old_arms
			return False
		else # If we made it here, the move was successful.
			return True
		
	def hit(self, base) # Need location of new pivot, new "arms," and base.
		# Mike: Take in direction search base matrix for location.
		# Mike: If the new location of the piece hits a 1, throw a violation.
		# Mike: Depending on the violation it either does not move or it gets absorbed.
		if column = column:
			# Mike: loop through arms and check base rows to see if there is a violation.
			# Mike: if violation then (??? typically the game has a pause for you to change it move)
			# Mike: loop thru arms loop thru columns.  If they == base location then return 1		
		elif row = row:
			# Mike: loop through arms and check base rows to see if there is a violation.
			# Mike: if violation then (??? typically the game has a pause for you to change it move)
			for arm in self.arms
				# Mike: loop thru arms loop thru rows.  If they == base location then return 2

	def rotate(self):
		# TODO: matrix rotation
		for arm in self.arms
			self.arms(arm) = self.arms(arm) + 1


# Jono: Back to 'Base'.
class Base:

	def __init__(self, dimensions):
		# Width and height of the game board.
		self._dimensions = dimensions
		pass

	def delete_rows(self):
		pass

	def add_piece(self, piece):
		pass

	def is_game_over(self):
		pass
