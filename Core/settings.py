from os import get_terminal_size
from sys import platform

# SYSTEM CONSTANTS
TERM_SIZE = TERM_W, TERM_H = get_terminal_size()
OS_NAME = platform

# STANDARDS
STD_PROMPT    = "> "
STD_LINE_CHAR = "—"
STD_PAGE_SIZE = 8

# DEV
DEV_MODE = True
