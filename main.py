from rich import print
import yaml

from Core.managers import StateManager, DataManager
import Core.refs as ref
from Core.settings import DEV_MODE, TERM_W
from States.dev_st import *
from States.menus import *
from States.solo import *
from Utils.display import clr
from World.Items.items import Container, ItemBuilder, ItemObj
from World.Player.player import Player

# Load the whole item 'database'

with open('World/Items/itemdb.yml', 'r') as f:
    item_data = yaml.safe_load(f)

# Main Game class

class Game:
    def __init__(self):
        # States

        self.sm = StateManager(
            Start, Menu, Inventory, WIP, ItemList,
            Dev_Options
        )
        self.dm = DataManager()

        self.sm.go_to(ref.id_start_menu)

        # Game stuff

        self.items_data = item_data
        self.items = [ItemBuilder(i) for i in item_data.values()]
        self.player = Player(Container())

        self.running = True

    def end(self):
        self.running = False

    def run(self):
        # Main game loop

        while self.running:
            clr()
            if DEV_MODE:
                print("=- DEV MODE ON -=".center(TERM_W))
            try:
                self.sm.run(self)
            except KeyboardInterrupt:
                self.running = False


Game().run()
clr()
print("-Game Closed-")

