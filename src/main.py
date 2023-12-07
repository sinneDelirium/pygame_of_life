#!/usr/bin/env python
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_MINUS,
    K_EQUALS,
    KEYDOWN,
    QUIT
)

WIDTH = 800
HEIGHT = 600


class Game:
    def __init__(self):
        self.running = True
        self.display_surf = None
        self.size = self.weight, self.height = WIDTH, HEIGHT
 
    def init(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True
 
    def event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def loop(self):
        pass

    def render(self):
        pass

    def cleanup(self):
        pygame.quit()

    def execute(self):
        if self.init() == False:
            self.running = False

        while(self.running):
            for event in pygame.event.get():
                self.event(event)
            self.loop()
            self.render()
        self.cleanup()


if __name__ == "__main__" :
    game = Game()
    game.execute()
