#== Global dependencies
import tensorflow as tf
import pygame, sys
import random

from pygame.locals import *
#==

from . import Agents

class AnnE:
    def __init__(self, config):
        self.config = config
        self.surface = pygame.display.set_mode(config["size"])
        self.agents = []

    def add_agent(self):
        self.agents.append(Agents.Agent_0(self.__random_pos()))

    def run(self):
        pygame.init()

        frames = 0
        prev_time = pygame.time.get_ticks()
        while True:
            # game logic computations go here
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # rendering
            self.__draw()

            # fps monitoring
            # based on fps_cap and time
            frames += 1
            elapsed_time = pygame.time.get_ticks() - prev_time
            if (elapsed_time >= 1000):
                frames = 0
                prev_time = pygame.time.get_ticks()
            else:
                if (frames == self.config["fps_cap"]):
                    print("f: %d" % frames)
                    print("e: %d" % elapsed_time)
                    frames = 0

                    wait_time = int((1000 - elapsed_time) * 1)
                    pygame.time.wait(wait_time)

    # PRIVATE
    def __draw(self):
        self.__draw_terrain()
        self.__draw_agents()
        pygame.display.update()

    def __draw_terrain(self):
        pygame.draw.rect(self.surface, (255,255,255), (0,0, self.config["size"][0], self.config["size"][1]))

    def __draw_agents(self):
        for agent in self.agents:
            agent.draw(self.surface)

    # helper functions
    def __random_pos(self):
        return [random.randint(0, self.config["size"][0]), random.randint(0, self.config["size"][1])]

