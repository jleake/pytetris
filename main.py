from wrapper.wrapper import curses_wrapper;
from wrapper.cg import CursesGraphics;
from game import *;

def main(cg):
	for n in range(1, 30):
		cg.draw('#', (CursesGraphics.RED, CursesGraphics.BLACK), [(n, 1), (n, 2), (n, 3), (n+1, 3)]);
		cg.refresh();
		cg.wait_for_key(1000);
		cg.erase([(n, 1), (n, 2), (n, 3), (n+1, 3)]);

# Call the main curses wrapper function to start things off. The parameter refers to the main function to be run after curses initialization. (In this case, this is the above "main" function.)
curses_wrapper(main);
