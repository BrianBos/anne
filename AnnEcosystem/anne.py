import time
import sys
import random

from . import Actions
from . import Agents
from . import Gui

class AnnE:

    def __init__(self, config):
        # init variables
        self.agents = []
        self.config = config

        # set up required modules
        #   Gui, Movement
        gui_config = self.__pluck(config, ["size"])
        self.gui = Gui.DefaultGui(self, gui_config)

        # setup test agents
        new_agent = Agents.Agent_0(self, self.__random_pos())
        new_agent.add_action(Actions.PyGame.Step2D(new_agent))
        self.agents.append(new_agent)

    def run(self):
        frames = 0
        prev_time = time.time()

        # game loop
        while True:
            if (frames % 30 == 0):
                self.agents[0].act()
            # game logic computations go here
            if self.gui.quit():
                sys.exit()

            # rendering
            self.gui.render()

            # fps monitoring
            # based on fps_cap and time
            frames += 1
            elapsed_time = time.time() - prev_time
            if (elapsed_time >= 1.0):
                frames = 0
                prev_time = time.time()
            else:
                if (frames == self.config["fps_cap"]):
                    print("f: %d" % frames)
                    print("e: %f" % elapsed_time)
                    frames = 0

                    wait_time = (1.0 - elapsed_time) * 1.0
                    time.sleep(wait_time)

    # HELPERS:
    def __random_pos(self): return [random.randint(0, self.config["size"][0]), random.randint(0, self.config["size"][1])]

    def __pluck(self, d, keys):
        new_dict = {}
        for i in range(len(keys)):
            new_dict[keys[i]] = d[keys[i]]
        return new_dict

