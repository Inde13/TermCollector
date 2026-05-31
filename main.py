from rich import inspect, print
import yaml

import Core.refs as ref
from World.Items.items import Container, ItemBuilder, ItemObj
from States.base import State, StateManager
from States.common import *
from Utils.display import clr
from World.Player.player import Player


# Load the whole item 'database'

with open('World/Items/itemdb.yml', 'r') as f:
    item_data = yaml.safe_load(f)

# Main Game class

class Game:
    def __init__(self):
        # States

        self.sm = StateManager(
            Start(), Menu(), Inventory(), WIP()
        )

        self.sm.go_to(ref.id_start_menu)

        # Game stuff

        self.items = [ItemBuilder(i) for i in item_data.values()]
        self.player = Player(Container())

        self.running = True

    def end(self):
        self.running = False

    def run(self):
        # Main game loop

        while self.running:
            clr()

            self.sm.run(self)
            self.sm.update(self)


Game().run()


