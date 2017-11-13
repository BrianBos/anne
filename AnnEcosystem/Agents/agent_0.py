#== Global dependencies
import tensorflow as tf
import pygame, sys
import random

from pygame.locals import *
#==

# Base agent
# contains the basic functions needed to operate in the ecosystem
class Agent_0:
    def __init__(self, pos):
        self.id = "agent_0"
        self.eco = 200
        self.position = pos

    def draw(self, surf):
        pygame.draw.circle(surf, (0,255,0), self.position, 5)

