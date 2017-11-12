#== Global dependencies
import tensorflow as tf
import pygame, sys
import random

from pygame.locals import *
#==

class Agent_0:
    def __init__(self, pos):
        self.id = "agent_0"
        self.position = pos

    def draw(self, surf):
        pygame.draw.circle(surf, (0,255,0), self.position, 5)

