#== Global dependencies
import pygame
#==

# Base agent
# contains the basic functions needed to operate in the ecosystem
class Agent_0:
    def __init__(self, anne, pos):
        self.anne = anne
        self.eco = 200
        self.position = pos

        # Mutable attributes
        self.geometry = ["circle", [5]]
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    # TODO: set this to accept action index so different actions
    #       can be used from this function
    def act(self):
        if (len(self.actions) == 0):
            return False
        self.actions[0].do()
        return True
