import curses

class CursesGraphics:

	BLACK = curses.COLOR_BLACK
	RED = curses.COLOR_RED
	WHITE = curses.COLOR_WHITE

	# (fg, bg) -> curses color pair number
	_color_pair_dictionary = {(WHITE, BLACK): 0}

	_next_color_pair = 1

	def __init__(self, window):
		# Make cursor invisible.
		curses.curs_set(0)

		# Main curses screen.
		self._window = window

		# Bold characters (colors are brighter).
		self._window.attron(curses.A_BOLD)

	def draw(self, character, color_pair, locations):
		color_pair_number = CursesGraphics._get_color_pair_number(color_pair)
		color_attributes = curses.color_pair(color_pair_number)

		for rc in locations:
			row = rc[0]
			column = rc[1]

			self._window.addch(row, column, character, color_attributes)

	def erase(self, locations):
		for rc in locations:
			row = rc[0]
			column = rc[1]

			# AND'ing with -256 strips out the character, leaving just the attributes. (The idea is that we put a space with the same background color as the previous character.)
			attributes = self._window.inch(row, column) & -256

			self._window.addch(row, column, ' ', attributes)

	def refresh(self):
		self._window.refresh()

	def wait_for_key(self, milliseconds = -1):
		self._window.timeout(milliseconds)
		return self._window.getch()

	@classmethod
	def _get_color_pair_number(cls, color_pair):
		cpd = cls._color_pair_dictionary

		foreground_color = color_pair[0]
		background_color = color_pair[1]

		if (color_pair not in cpd):
			curses.init_pair(cls._next_color_pair, foreground_color, background_color)
			cpd[color_pair] = cls._next_color_pair
			cls._next_color_pair += 1

		return cpd[color_pair]


# Calls the "real" main function, sending a CursesGraphics object.
def _wrapper_helper(stdscr, main_function):
	cg = CursesGraphics(stdscr)
	main_function(cg)

# Wrapper for the main function does setup and cleanup for curses.
def curses_wrapper(main_function):
	curses.wrapper(_wrapper_helper, main_function)

