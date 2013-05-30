from wrapper.cg import CursesGraphics;
from game import *;

def main(cg):
	draw_ch = '#';
	for n in range(1, 30):
		cg.draw(draw_ch, (CursesGraphics.RED, CursesGraphics.BLACK), [(n, 1), (n, 2), (n, 3), (n+1, 3)]);
		cg.refresh();
		new_ch = cg.wait(1000);

		if (new_ch > 0):
			draw_ch = new_ch;

		cg.erase([(n, 1), (n, 2), (n, 3), (n+1, 3)]);
