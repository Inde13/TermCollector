from os import get_terminal_size
from sys import platform

import curses

# Curses
stdscr = curses.initscr()
stdscr.nodelay(1)
curses.cbreak()
curses.start_color()
curses.use_default_colors()
curses.curs_set(0)

H, W = stdscr.getmaxyx()


# SYSTEM CONSTANTS
TERM_SIZE = TERM_W, TERM_H = get_terminal_size()
OS_NAME = platform

# STANDARDS
STD_PROMPT    = "> "
STD_LINE_CHAR = "—"
STD_PAGE_SIZE = 8

# DEV
DEV_MODE = False
killmode = False
