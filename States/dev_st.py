from rich import print
import yaml

from .base import State
import Core.refs as ref
from Core.settings import STD_PROMPT
from Utils.display import *
from Utils.pager import Pager


class Dev_Options(State):
    id = ref.id_dev_options

    def __init__(self):
        super().__init__()

    def run(self, ctx):
        options = ["Item Manager", "Back"]

        display_title("Dev_Options")
        option_menu(options)

        match input(STD_PROMPT):
            case "1":
                ctx.sm.go_to(ref.id_dev_imngr)
            case "2":
                ctx.sm.go_back()


class Dev_ItemManager(State):
    id = ref.id_dev_imngr

    def __init__(self):
        super().__init__()

    def run(self, ctx):
        items = ctx.items_data
        options = ["Back"]

        pager = Pager([i["name"] for i in items.values()])

        display_title("Dev_Item_Manager")
        pager.selector_mode()
        option_menu(options)

        match input(STD_PROMPT):
            case "1":
                ctx.sm.go_back()

