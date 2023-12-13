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

# 1. Any live cell with fewer than two live neighbours dies,
# as if by underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next
# generation.
# 3. Any live cell with more than three live neighbours dies,
# as if by overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell,
# as if by reproduction.

# Create outline around blocks themselves
# Add ability to add patterns with mouse

WIDTH = 800
HEIGHT = 600
FPS = 10
OSICILLATOR = [[1],
               [1],
               [1],
               [1]
               ]


class Game:
    def __init__(self):
        self.running = True
        self.display_surf = None
        self.size = self.width, self.height = WIDTH, HEIGHT
 
    def init(self):
        # Pygame initialization
        pygame.init()
        self.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Game of Life")
        self.running = True
        self.clock = pygame.time.Clock()
        # Initialize grid
        self.grid_width = 20
        self.grid_height = 20
        self.block_w = self.width / self.grid_width
        self.block_h = self.height / self.grid_height
        self.grid = [[0 for x in range(self.grid_width)] for y in range(self.grid_height)]
        self.add_pattern(0, 5, 5)
 
    def event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def next_gen(self):
        # Store previous generation
        grid = self.grid.copy()

        # Check number of neighbors for each cell
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                neighbors = self.count_neighbors(row, col, grid)
                # if (neighbors != 0): print(f'Neighbors: {neighbors} at {row}, {col}')
                # Depending on neighbors, follow rules of life


    def count_neighbors(self, row, col, grid):
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (row + i < 0 or
                    row + i > self.grid_height - 2 or
                    col + j < 0 or
                    col + j > self.grid_width - 2 or
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


if __name__ == "__main__" :
    game = Game()
    game.execute()
