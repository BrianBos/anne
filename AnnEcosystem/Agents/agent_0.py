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
        self.frame_cost = 10  # how long an action persists in frames
        self.nn = None

        # Mutable attributes
        self.geometry = ["circle", [5]]
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def add_nn(self, nn):
        self.nn = nn

    # TODO: set this to accept action index so different actions
    #       can be used from this function
    def act(self):
        assessed_action = self.nn.assess()[0]

        if (len(self.actions) == 0):
            return False
        self.actions[assessed_action].do()
        return True
