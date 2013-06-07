import curses
from cg import CursesGraphics

# Calls the "real" main function, sending a CursesGraphics object.
def _wrapper_helper(stdscr, main_function):
	cg = CursesGraphics(stdscr)
	main_function(cg)

# Wrapper for the main function does setup and cleanup for curses.
def curses_wrapper(main_function):
	curses.wrapper(_wrapper_helper, main_function)
