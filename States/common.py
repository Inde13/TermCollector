from .base import State
import Core.refs as ref
from Core.settings import STD_PROMPT
from Utils.display import option_menu, line, display_container
from Utils.items import get_random_item

class Start(State):
    def __init__(self):
        super().__init__(ref.id_start_menu)

    def run(self, ctx):
        options = ["Play", "Quit"]

        option_menu(options)

        match input(STD_PROMPT):
            case "1":
                ctx.sm.go_to(ref.id_main_menu)
            case "2":
                ctx.end()

class Menu(State):
    def __init__(self):
        super().__init__(ref.id_main_menu)

    def run(self, ctx):
        options = ["Items", "Inventory", "Back"]

        option_menu(options)

        match input(STD_PROMPT):
            case "1":
                ctx.sm.go_to(ref.id_items_list)
            case "2":
                ctx.sm.go_to(ref.id_inventory)
            case "3":
                ctx.sm.go_back()

class WIP(State):
    def __init__(self):
        super().__init__(ref.id_wip)

    def run(self, ctx):
        print("WIP: Coming soon")
        print("Press ENTER to go back")
        input()
        ctx.sm.go_back()


class Inventory(State):
    def __init__(self):
        super().__init__(ref.id_inventory)

    def run(self, ctx):
        options = ["Get random item", "Back"]
        inv_container = ctx.player.inventory

        display_container(inv_container)

        line()

        option_menu(options)

        match input(STD_PROMPT):
            case "1":
                item = get_random_item(ctx.items).build(
                        ctx.player.inventory)
                ctx.player.inventory.add(item)
            case "2":
                ctx.sm.go_back()


