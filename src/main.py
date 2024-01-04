#!/usr/bin/env python
import copy
import pygame
import random as r
from patterns import PATTERNS
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


# Create outline around blocks themselves (black outline with white interior)
# Implement wrap-around
# Add ability to add patterns with mouse
# Draw string with current generation
# Draw string with current pattern selection and category (still lifes, oscillators, spaceships, etc.)
# Draw outline around area that pattern will be placed using mouse
# Use middle mouse to pan and zoom, left click to place pattern, right click to cycle patterns


SCREEN_SIZE = (600, 600)
GRID_SIZE = (150, 150)
FPS = 30

class Game:
    def __init__(self):
        self.running = True
        self.display_surf = None
        self.size = self.screen_width, self.screen_height = SCREEN_SIZE


    def init(self):
        # Pygame initialization
        pygame.init()
        self.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Game of Life")
        self.running = True
        self.clock = pygame.time.Clock()
        # Initialize grid
        self.grid_width, self.grid_height = GRID_SIZE
        self.block_w = self.screen_width / self.grid_width
        self.block_h = self.screen_height / self.grid_height
        self.grid = [[0 for x in range(self.grid_width)] for y in range(self.grid_height)]

        # Add funky patterns
        self.add_funky_pattern()


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


    def fill_area(self, row, col, width, height, state):
        # Fill area with state-based cells
        for i in range(height):
            for j in range(width):
                self.grid[row + i][col + j] = state


    def add_pattern(self, pattern, row, col):
        pattern_width = len(pattern[0])
        pattern_height = len(pattern)

        # Check if pattern is fully within grid
        if row + pattern_height > self.grid_height or col + pattern_width > self.grid_width:
            return

        # Make sure pattern exists and then add it to grid
        if pattern:
            # Fill background area and one layer border with 0s
            self.fill_area(row, col, pattern_width, pattern_height, 0)
            # Fill pattern area with 1s
            for i in range(pattern_height):
                for j in range(pattern_width):
                    self.grid[row + i][col + j] = pattern[i][j]


    def add_funky_pattern(self):
        for i in range(-10, 10):
            for j in range(-10, 10):
                self.add_pattern(PATTERNS["pulsar"],
                                 self.grid_width // 2 + r.randint(-10, 10),
                                 self.grid_height // 2 + r.randint(-10, 10))


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
