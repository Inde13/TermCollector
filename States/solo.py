from rich import print
import curses

from .base import State
import Data.datakeys as dk
import Data.refs as ref
from Data.settings import *
from Utils.display import option_menu, line, display_container, display_title, display_warning_box
from Utils.items import get_random_item
from Utils.pager import Pager


class WIP(State):
    id = ref.id_wip

    def __init__(self):
        super().__init__()

    def run(self, ctx):
        stdscr.addstr("WIP: Coming soon\n")
        stdscr.addstr("Press anything to go back")
        stdscr.nodelay(0)
        stdscr.getch()
        stdscr.nodelay(1)
        ctx.sm.go_back()


class Inventory(State):
    id = ref.id_inventory

    def __init__(self):
        super().__init__()

    def run(self, ctx):
        options = ["Get random item", "Back"]
        inv_container = ctx.player.inventory

        display_title("Inventory")

        display_container(inv_container)

        option_menu(options)

        key = stdscr.getch()
        if key == ord("1"):
            item = get_random_item(ctx.items).build(
                    ctx.player.inventory)
            ctx.player.inventory.add(item)
        elif key == ord("2"):
            ctx.sm.go_back()


class ItemList(State):
    id = ref.id_items_list

    def __init__(self):
        super().__init__()
        self.pager = None

    def run(self, ctx):
        if ctx.dm.has(dk.SELECTION_VALUE):
            ctx.dm.add(
                    dk.WARNING_BOX_MSG,
                    "Item cards are not avaiable in this version"
            )
            ctx.dm.remove(dk.SELECTION_VALUE)

        items = ctx.player.inventory.get()
        items = [f"{i.name} ({i.quantity}x)" for i in items]
        if self.pager is None or self.pager.data != items:
            self.pager = Pager(items)

        display_title("Item List")

        self.pager.display_current()

        options = ["Item Card", "Back"]
        option_menu(options)

        display_warning_box(ctx.dm.get(dk.WARNING_BOX_MSG))
        ctx.dm.remove(dk.WARNING_BOX_MSG)

        key = stdscr.getch()
        if key == ord("1"):
            self.pager.selector_mode(ctx, dk.SELECTION_VALUE)
        elif key == ord("2"):
            ctx.sm.go_back()

