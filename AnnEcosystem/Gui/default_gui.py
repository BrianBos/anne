#== Global dependencies
import pygame, sys
import random

from pygame.locals import *
#==

# Default Gui that uses pygame to render frames
class DefaultGui:
    def __init__(self, anne, config):
        self.anne = anne
        self.config = config

        self.surface = pygame.display.set_mode(self.config["size"])
        pygame.init()

    # method to render one frame
    def render(self):
        self.__draw_terrain()
        self.__draw_agents()
        pygame.display.update()

    def quit(self):
        for event in self.events():
            if event.type == QUIT:
                pygame.quit()
                return True
        return False

    def events(self):
        return pygame.event.get()

    # PRIVATE:
    def __draw_terrain(self):
        pygame.draw.rect(self.surface, (236, 240, 241), (0,0, self.config["size"][0], self.config["size"][1]))

    def __draw_agents(self):
        for agent in self.anne.agents:
            agent.draw(self.surface)
