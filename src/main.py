#!/usr/bin/env python
import copy
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

# Create outline around blocks themselves
# Add ability to add patterns with mouse
# Add maps from file
# Convert to HashLife algorithm
# Allow for comparisons between algorithms (ms between frames)
# Eventually convert to golly's .mc file format from 2D array

SIZE = 600
FPS = 10
OSICILLATOR = [[1],
               [1],
               [1]
               ]


class Game:
    def __init__(self):
        self.running = True
        self.display_surf = None
        self.size = self.width, self.height = SIZE, SIZE


    def init(self):
        # Pygame initialization
        pygame.init()
        self.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Game of Life")
        self.running = True
        self.clock = pygame.time.Clock()
        # Initialize grid
        self.grid_width = 10
        self.grid_height = 10
        self.block_w = self.width / self.grid_width
        self.block_h = self.height / self.grid_height
        self.grid = [[0 for x in range(self.grid_width)] for y in range(self.grid_height)]
        self.add_pattern(0, 5, 5)


    def event(self, event):
        if event.type == pygame.QUIT:
            self.running = False


    def next_gen(self):
        # Store previous generation
        grid = copy.deepcopy(self.grid)

        # Check number of neighbors for each cell
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                neighbors = self.count_neighbors(row, col, grid)
                alive = grid[row][col]
                # Depending on neighbors, follow rules of life
                if ((neighbors == 2 or neighbors == 3) and alive == 1): 
                    self.grid[row][col] = 1 # survives due to 2/3 neighbors
                elif (neighbors == 3 and alive == 0):
                    self.grid[row][col] = 1 # becomes alive due to 3 neighbors
                else:
                    self.grid[row][col] = 0 # dies due to under/overpopulation


    def count_neighbors(self, row, col, grid):
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (row + i < 0 or
                    row + i > self.grid_height - 1 or
                    col + j < 0 or
                    col + j > self.grid_width - 1 or
                    (i == 0 and j == 0)): continue
                else:
                    neighbors += grid[row + i][col + j]
        return neighbors


    def add_pattern(self, pattern, row, col):
        if pattern == 0:
            for i in range(len(OSICILLATOR)):
                for j in range(len(OSICILLATOR[i])):
                    self.grid[row + i][col + j] = OSICILLATOR[i][j]


    def render(self):
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                color = (255,255,255)
                if self.grid[row][col] == 1:
                    color = (0,0,0)
                rect = pygame.Rect(col * self.block_w,
                                   row * self.block_h,
                                   self.block_w, self.block_h)
                pygame.draw.rect(self.display_surf, color, rect)
        pygame.display.flip()


    def cleanup(self):
        pygame.quit()


    def execute(self):
        if self.init() == False:
            self.running = False

        while(self.running):
            # Event handling
            for event in pygame.event.get():
                self.event(event)
            self.next_gen()
            self.render()
            self.clock.tick(FPS)
        self.cleanup()


if __name__ == "__main__":
    game = Game()
    game.execute()
