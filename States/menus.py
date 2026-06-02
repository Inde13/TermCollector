from rich import print

from .base import State
import Core.refs as ref
from Core.settings import STD_PROMPT, DEV_MODE
from Utils.display import option_menu, display_title


class Start(State):
    id = ref.id_start_menu
    def __init__(self):
        super().__init__()

    def run(self, ctx):
        options = ["Play", "Quit"]
        if DEV_MODE: options = ["Play", "Dev", "Quit"]

        display_title("Main Menu")

        option_menu(options)

        match input(STD_PROMPT):
            case "1":
                ctx.sm.go_to(ref.id_main_menu)
            case "2" if not DEV_MODE:
                ctx.end()
            case "2" if DEV_MODE:
                ctx.sm.go_to(ref.id_dev_options)
            case "3" if DEV_MODE:
                ctx.end()


class Menu(State):
    id = ref.id_main_menu
    def __init__(self):
        super().__init__()

    def run(self, ctx):
        options = ["Items", "Inventory", "Back"]

        display_title("Game Menu")

        option_menu(options)

        match input(STD_PROMPT):
            case "1":
                ctx.sm.go_to(ref.id_items_list)
            case "2":
                ctx.sm.go_to(ref.id_inventory)
            case "3":
                ctx.sm.go_back()


