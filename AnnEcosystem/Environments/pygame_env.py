#== Global dependencies
import pygame
import random

from pygame.locals import *
#==

# Default Environment that uses pygame
class PygameEnv:
    def __init__(self, anne, config):
        self.anne = anne
        self.env_config = config

        self.surface = pygame.display.set_mode(self.env_config["size"])
        pygame.init()

    # function to render one frame
    def render(self):
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
                (0,0, self.env_config["size"][0], self.env_config["size"][1]))

    def __draw_agents(self):
        for agent in self.anne.agents:
            if (agent.geometry[0] == "circle"):
                pygame.draw.circle(self.surface, (0,255,0), agent.position, agent.geometry[1][0])
