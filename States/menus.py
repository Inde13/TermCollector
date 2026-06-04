import curses
from rich import print
from yaml import safe_load

from .base import State
import Data.refs as ref
from Data.settings import *
from Utils.display import option_menu, display_title


class TitleScreen(State):
    id = ref.id_title_screen

    def __init__(self):
        super().__init__()

    def run(self, ctx):
        art = ctx.art["GameTitle"]
        press_txt = "Press anything to start"

        for y, line in enumerate(art):
            stdscr.addstr(y, W//2-len(line)//2, line + "\n")
        stdscr.addstr(y+3, W//2-len(press_txt)//2, press_txt)

        stdscr.nodelay(0)
        stdscr.getch()
        stdscr.nodelay(0)
        ctx.sm.go_to(ref.id_start_menu)


class Start(State):
    id = ref.id_start_menu

    def __init__(self):
        super().__init__()

    def run(self, ctx):
        options = ["Play", "Quit"]
        if DEV_MODE: options = ["Play", "Dev", "Quit"]

        display_title("Main Menu")

        option_menu(options)

        key = stdscr.getch()
        if key == ord("1"):
            ctx.sm.go_to(ref.id_main_menu)
        elif key == ord("2") and not DEV_MODE:
            ctx.end()
        elif key == ord("2"):
            ctx.sm.go_to(ref.id_dev_options)
        elif key == ord("3") and DEV_MODE:
            ctx.end()


class Menu(State):
    id = ref.id_main_menu

    def __init__(self):
        super().__init__()

    def run(self, ctx):
        options = ["Items", "Inventory", "Back"]

        display_title("Game Menu")

        option_menu(options)

        key = stdscr.getch()
        if key == ord("1"):
            ctx.sm.go_to(ref.id_items_list)
        elif key == ord("2"):
            ctx.sm.go_to(ref.id_inventory)
        elif key == ord("3"):
            ctx.sm.go_back()

