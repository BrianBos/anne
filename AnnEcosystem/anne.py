import sys
import random

from .Games import PyWildInt
from .evo_engine import EvoEngine

class AnnE:
    def __init__(self, config):
        # init variables
        self.agents = []
        self.config = config

        # replacement for time since processing
        # speed varies a lot
        # used for time(tick) dependent methods
        self.ticks = 0

        # initialize required modules
        # init game
        game_config = self.__pluck(config["game"], ["size"])
        self.game = PyWildInt(self, game_config)
        self.game_actions = self.game.actions
        self.game_agents = self.game.agents
        # evolution engine
        self.evo_engine = EvoEngine(self)

        # setup test agents
        self.__populate()

    def run(self):
        # game loop
        while True:
            if self.game.quit():
                sys.exit()
            print(self.ticks)

            for agent in self.agents:
                agent.act()
                agent.decay()

            self.game.step()
            self.ticks += 1

    # HELPERS:
    def __random_pos(self): return [random.randint(0, self.config["game"]["size"][0] - 20), random.randint(0, self.config["game"]["size"][1] - 20)]

    def __pluck(self, d, keys):
        new_dict = {}
        for i in range(len(keys)):
            new_dict[keys[i]] = d[keys[i]]
        return new_dict

    def __populate(self):
        # add 'food' agents ie source of energy
        for _ in range(20):
            new_agent = self.game_agents[0](self, self.__random_pos())
            self.agents.append(new_agent)
        
        # add mobile agent
        for _ in range(5):
            new_agent = self.game_agents[1](self, self.__random_pos())
            self.evo_engine.seed(new_agent)
            self.agents.append(new_agent)