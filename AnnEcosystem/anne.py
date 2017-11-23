import time
import sys
import random

from .Games import PyWildInt
from . import NeuralNetworks

class AnnE:
    def __init__(self, config):
        # init variables
        self.agents = []
        self.config = config

        # initialize required modules
        # init game
        game_config = self.__pluck(config["game"], ["size"])
        self.game = PyWildInt(self, game_config)
        self.game_actions = self.game.actions
        self.game_agents = self.game.agents

        # setup test agents
        self.__populate()

    def run(self):
        prev_time = time.time()

        # game loop
        while True:
            if self.game.quit():
                sys.exit()

            elapsed_time = time.time() - prev_time
            if (elapsed_time >= 1.0):
                prev_time = time.time()
                continue

            # TODO: add actions/sec functionality
            # run agent actions depending on their frame cost
            for agent in self.agents:
                agent.act()

            self.game.step()

    # HELPERS:
    def __random_pos(self): return [random.randint(0, self.config["game"]["size"][0] - 20), random.randint(0, self.config["game"]["size"][1] - 20)]

    def __pluck(self, d, keys):
        new_dict = {}
        for i in range(len(keys)):
            new_dict[keys[i]] = d[keys[i]]
        return new_dict

    def __populate(self):
        for _ in range(20):
            new_agent = self.game_agents[0](self, self.__random_pos())
            # new_agent.add_nn(NeuralNetworks.TensorFlowNN.Dense({"dna": [4, [3, 2], 4]}))
            self.agents.append(new_agent)
        
        new_agent = self.game_agents[1](self, self.__random_pos())
        new_agent.add_action(self.game_actions[0](new_agent))
        new_agent.add_action(self.game_actions[1](new_agent))
        new_agent.add_action(self.game_actions[2](new_agent))
        new_agent.add_action(self.game_actions[3](new_agent))
        new_agent.add_nn(NeuralNetworks.TensorFlowNN.Dense({"dna": [4, [3, 2], 4]}))
        self.agents.append(new_agent)