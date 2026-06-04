import curses
from rich import print
import yaml

from Data.managers import StateManager, DataManager
import Data.refs as ref
from Data.settings import *
from States.dev_st import *
from States.menus import *
from States.solo import *
from Utils.display import clr
from World.Items.items import Container, ItemBuilder, ItemObj
from World.Player.player import Player


# Load the whole item 'database'

with open('World/Items/itemdb.yml', 'r') as f:
    item_data = yaml.safe_load(f)

# Load the game art

with open("Data/art.yml", "r") as f:
    art = yaml.safe_load(f)

# Main Game class

class Game:
    def __init__(self):
        self.sm = StateManager(
            Start, Menu, Inventory, WIP, ItemList,
            Dev_Options, TitleScreen
        )
        self.dm = DataManager()

        self.sm.go_to(ref.id_title_screen)

        # World

        self.items_data = item_data
        self.items = [ItemBuilder(i) for i in item_data.values()]
        self.player = Player(Container())

        # Game

        self.art = art
        self.running = True

    def end(self):
        self.running = False

    def run(self, stdscr):
        # Main game loop

        while self.running and not killmode:
            stdscr.erase()
            if DEV_MODE: pass
                # print("=- DEV MODE ON -=".center(TERM_W))
            try:
                self.sm.run(self)
            except KeyboardInterrupt:
                self.running = False


curses.wrapper(Game().run)
clr()
print("-Game Closed-")

