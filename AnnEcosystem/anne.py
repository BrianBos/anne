import sys
import random

from .Ecosystems import PyWildInt
from . import NeuralNetworks
from .genetics import Genetics

class Anne:
  def __init__(self, config):
    # init variables
    self.agents = []
    self.config = config

    # replacement for time since processing
    # speed varies a lot
    # used for time(tick) dependent methods
    self.ticks = 0

    # initialize required modules
    # init ecosystem
    eco_config = self.__pluck(config["ecosystem"], ["size"])
    self.ecosystem = PyWildInt(self, eco_config)
    # genetics engine
    self.genetics = Genetics(self)

    # setup test agents
    self.__populate()

  def run(self):
  # ecosystem loop
    while True:
      if self.ecosystem.quit():
        sys.exit()
      print(self.ticks)

      for agent in self.agents:
        agent.act()
        agent.decay()

      self.ecosystem.step()
      self.ticks += 1

  # HELPERS:
  def __random_pos(self): return [random.randint(0, self.config["ecosystem"]["size"][0] - 20), random.randint(0, self.config["ecosystem"]["size"][1] - 20)]

  def __pluck(self, d, keys):
    new_dict = {}
    for i in range(len(keys)):
      new_dict[keys[i]] = d[keys[i]]
    return new_dict

  def __populate(self):
  # add 'food' agents ie source of energy
    for _ in range(20):
      new_agent = self.ecosystem.agents[0](self, self.__random_pos())
      self.agents.append(new_agent)
    
    # add mobile agent
    for _ in range(5):
      new_agent = self.ecosystem.agents[1](self, self.__random_pos())
      self.genetics.seed(new_agent)
      self.__flesh_out(new_agent)
      self.agents.append(new_agent)

  # method to add sensors and actions to agent
  def __flesh_out(self, agent):
    actions_num = self.genetics.actions_num(agent)

		# ADD ACTION
    for i in range(actions_num):
      agent.actions.append(self.ecosystem.action_pool[i](agent))
		
		# ADD NEURAL NETWORK
    agent.nn = NeuralNetworks.TensorFlowNN.Dense(self.genetics.nn_config(agent))
    return