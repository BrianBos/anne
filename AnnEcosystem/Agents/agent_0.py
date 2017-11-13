#== Global dependencies
import tensorflow as tf
import pygame, sys
import random

from pygame.locals import *
#==

# Base agent
# contains the basic functions needed to operate in the ecosystem
class Agent_0:
    def __init__(self, anne, pos):
        self.anne = anne
        self.eco = 200
        self.position = pos

        self.actions = []
        self.action_opts = []

    def draw(self, surf):
        pygame.draw.circle(surf, (0,255,0), self.position, 5)

    def add_action(self, action):
        self.actions.append(action)
        # TODO: add mutation on action options
        self.action_opts.append(action.options[0])

    # TODO: set this to accept action index so different actions
    #       can be used from this function
    def act(self):
        self.actions[0].do()
