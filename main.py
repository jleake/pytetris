import curses;
from wrapper.cg import CursesGraphics;
from run import main;

# Calls the "real" main function in the 'run' module (see 'run.py').
def _main_wrapper(stdscr):
	cg = CursesGraphics(stdscr);
	main(cg);

# Wrapper for the main function does setup and cleanup for curses.
curses.wrapper(_main_wrapper);
