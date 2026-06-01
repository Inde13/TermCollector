from .base import State
import Core.refs as ref
from Core.settings import STD_PROMPT, TERM_W
from Utils.display import option_menu, line, display_container
from Utils.items import get_random_item
from Utils.pager import Pager

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


class ItemList(State):
    def __init__(self):
        super().__init__(ref.id_items_list)
        self.pager = None

    def run(self, ctx):
        items = ctx.player.inventory.get()
        items = [f"{i.name} ({i.quantity}x)" for i in items]
        if self.pager is None or self.pager.data != items:
            self.pager = Pager(items)

        self.pager.selector_mode()

        line()
        print("Enter 'w' or 's' to move the cursor")
        print("Enter 'a' or 'd' to move the pages")

        options = ["Select", "Back"]
        option_menu(options)

        page_amount = self.pager.page_amount

        match input(STD_PROMPT):
            case "1" if page_amount > 0:
                cursor = self.pager.cursor
                ctx.dm.add(
                    "page_item",
                    self.pager.pages[current][cursor])
                ctx.sm.go_back()
            case "2":
                self.pager.cursor = 0
                self.pager.current = 0
                ctx.sm.go_back()
            case "a" if page_amount > 0:
                self.pager.back_page()
            case "d" if page_amount > 0:
                self.pager.next_page()
            case "w" if page_amount > 0:
                self.pager.cursor_up()
            case "s" if page_amount > 0:
                self.pager.cursor_down()


