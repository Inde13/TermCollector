from rich import print

from .base import State
import Core.datakeys as dk
import Core.refs as ref
from Core.settings import STD_PROMPT, TERM_W
from Utils.display import option_menu, line, display_container, display_title, display_warning_box
from Utils.items import get_random_item
from Utils.pager import Pager


class WIP(State):
    id = ref.id_wip
    def __init__(self):
        super().__init__()

    def run(self, ctx):
        print("WIP: Coming soon")
        print("Press ENTER to go back")
        input()
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

        match input(STD_PROMPT):
            case "1":
                item = get_random_item(ctx.items).build(
                        ctx.player.inventory)
                ctx.player.inventory.add(item)
            case "2":
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

        match input(STD_PROMPT):
            case "1" if not self.pager.is_empty():
                self.pager.selector_mode(ctx, dk.SELECTION_VALUE)
            case "2":
                ctx.sm.go_back()

