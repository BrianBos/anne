#== Global dependencies
import pygame
import random

from pygame.locals import *

from .PyWild import Actions
from .PyWild import Agents
#==

# Sample game that uses pygame
class PyWildInt:
  # provide list of available agents and actions
  # to enable anne evolve the agents by adding actions
  agents = [Agents.Agent_0, Agents.Agent_1]
  action_pool = [Actions.Up, Actions.Down, Actions.Left, Actions.Right]

  def __init__(self, anne, config):
    self.anne = anne
    self.game_config = config

    self.surface = pygame.display.set_mode(self.game_config["size"])
    pygame.init()
    
  # function to render one frame
  def step(self):
    self.__draw_terrain()
    self.__draw_agents()
    pygame.display.update()

  # method to check if user quit
  def quit(self):
    for event in self.events():
      if event.type == QUIT:
        pygame.quit()
        return True
    return False

  # function to obtain user events from pygame
  def events(self):
    return pygame.event.get()

  # PRIVATE:
  def __draw_terrain(self):
    pygame.draw.rect(
        self.surface,
        (236, 240, 241),
        (0,0, self.game_config["size"][0], self.game_config["size"][1]))

  def __draw_agents(self):
    for agent in self.anne.agents:
      # confine agents to game bounds
      self.__confine_to_bounds(agent)

      if (agent.skin["type"] == "circle"):
        pygame.draw.circle(self.surface, agent.skin["color"], agent.position, agent.skin["radius"])
  
  # method to confine agent to bounds
  def __confine_to_bounds(self, agent):
    if (agent.position[0] < 0):
      agent.position[0] = 5
    if (agent.position[1] < 0):
      agent.position[1] = 5
    if (agent.position[0] > self.game_config["size"][0]):
      agent.position[0] = self.game_config["size"][0] - 5
    if (agent.position[1] > self.game_config["size"][1]):
      agent.position[1] = self.game_config["size"][1] - 5
