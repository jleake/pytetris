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
			self.rotate(self) #rotate to the right

		# If we have a collision, revert to old pivot.
		if self.hit(self, direction, base) == 1:
			self.pivot = old_pivot
			self.arms = old_arms
			base.add_piece(base, self)
		elif self.hit(self, direction, base) == 2:	
			self.pivot = old_pivot
			self.arms = old_arms
			return False
		else # If we made it here, the move was successful.
			return True
		
	def hit(self, direction, base) 
		# Take in direction search base matrix for location.
		# If the new location of the piece hits a number, throw a violation.
		# Depending on the violation it either does not move or it gets absorbed.
			
		if direction == DOWN:
			for arm in self.arms
				# loop thru arms.  If they == base location then return 2
				for each arm in self.arms
					if self.arms(arm) == base.matrix(arms):
						return 2
		else
			for each arm in self.arms
				# If arm hits (but the piece isn't moving down), then just revert to old piece location.
					if self.arms(arm) == base.matrix(arms):
						return 1

	def rotate(self):
		# TODO: matrix rotation
		# Mike: the arms are just one number that represent the direction from the pivot (1 = the right of pivot)
		# Mike: the numbers go around in a circle so if you just add one
		# Mike: they will end up in the same place, except for when the circle has been completed
		for each arm in self.arms
			if self.arms(arm) + 1 == 5: # Circle complete go back to start
				self.arms(arm) = 1
			elif self.arms(arm) + 1 == 9:
				self.arms(arm) = 5
			elif self.arms(arm) + 1 == 13:
				self.arms(arm) = 9
			else:
				self.arms(arm) = self.arms(arm) + 1

class Base:

	def __init__(self, dimensions):
		# Mike: width and height of the terminal screen, plus a 'border'
		# Mike: the border consists of 1s and the rest of the board 0s.
		# Mike: as pieces 'hit' they turn into numbers (representing colors)
		self._dimensions = dimensions
		self.matrix # matrix of number codes signifying pieces
		pass

	def delete_rows(self):
		pass
		for check_row = 1 to self._dimensions(1):
			for check_col = 1 to self._dimensions(2):
				if self.matrix(check_row,check_col) !== 0:
					numbers = numbers + 1
			if numbers == self._dimensions(2) 
				for check_row_temp = check_row to self._dimensions(1) step -1:
					if check_row_temp !== 0:
						for check_col_temp = 1 to self._dimensions(2)
							self.matrix(check_row_temp,check_col_temp) = self.matrix(check_row_temp - 1,check_col_temp)
					elif check_row_temp == 0:
						for check_col_temp = 1 to self._dimensions(2)
							self.matrix(check_row_temp,check_col_temp) = 0
				
	def add_piece(self, piece):
		pass

	def is_game_over(self):
		pass
