import time
import sys
import random

from . import Actions
from . import Agents
from . import Environments
from . import NeuralNetworks

class AnnE:

    def __init__(self, config):
        # init variables
        self.agents = []
        self.config = config

        # set up required modules
        #   Gui, Movement
        env_config = self.__pluck(config["environment"], ["size"])
        self.env = Environments.PygameEnv(self, env_config)

        # setup test agents
        new_agent = Agents.Agent_0(self, self.__random_pos())
        new_agent.add_action(Actions.PyGame.Up(new_agent))
        new_agent.add_action(Actions.PyGame.Down(new_agent))
        new_agent.add_action(Actions.PyGame.Left(new_agent))
        new_agent.add_action(Actions.PyGame.Right(new_agent))
        new_agent.add_nn(NeuralNetworks.TensorFlowNN.Dense({"dna": [4, [3, 2], 4]}))
        self.agents.append(new_agent)

    def run(self):
        frames = 0
        prev_time = time.time()

        # game loop
        while True:
            if self.env.quit():
                sys.exit()

            elapsed_time = time.time() - prev_time
            if (elapsed_time >= 1.0):
                frames = 0
                prev_time = time.time()
                continue
            elif (frames == self.config["environment"]["fps_cap"]):
                print("f: %d" % frames)
                print("e: %f" % elapsed_time)
                frames = 0

                wait_time = (1.0 - elapsed_time) * 1.0
                time.sleep(wait_time)
                prev_time = time.time()
                continue

            # TODO: add actions/sec functionality
            # run agent actions depending on their frame cost
            self.agents[0].act()

            self.env.render()

            frames += 1

    # HELPERS:
    def __random_pos(self): return [random.randint(0, self.config["environment"]["size"][0]), random.randint(0, self.config["environment"]["size"][1])]

    def __pluck(self, d, keys):
        new_dict = {}
        for i in range(len(keys)):
            new_dict[keys[i]] = d[keys[i]]
        return new_dict

