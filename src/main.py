#!/usr/bin/env python
import copy
import pygame
from patterns import PATTERNS
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_q,
    K_a,
    KEYDOWN,
    QUIT
)

# Currently working on:
# Need to fix add pattern function to add pattern to grid and outline around it
# Create outline around blocks themselves (black outline with white interior)
# Add ability to add patterns with mouse
# Draw string with current generation
# Draw string with current pattern selection and category (still lifes, oscillators, spaceships, etc.)
# Draw outline around area that pattern will be placed using mouse
# Use middle mouse to pan and zoom, left click to place pattern, right click to cycle patterns

GRID_SIZE = 1000
SCREEN_SIZE = (900, 600)
FRAMERATE = 10
BG_COLOR = (255, 255, 255)
FG_COLOR = (0, 0, 0)


class Game:
    def __init__(self):
        self.running = True
        self.display_surf = None
        self.size = self.width, self.height = SCREEN_SIZE


    def init(self):
        # Pygame initialization
        pygame.init()
        self.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Game of Life")
        self.running = True
        self.clock = pygame.time.Clock()

        # Initialize view and grid
        self.view_width, self.view_height = self.size
        self.grid_size = GRID_SIZE
        self.block_size = 1
        self.grid = [[0 for x in range(self.grid_size)] for y in range(self.grid_size)]

        # Initialize mouse pattern
        self.mouse_pattern = PATTERNS[0]

        # Initialize pan and zoom variables
        self.offset_x = -self.view_width / 2 # want 0,0 as center
        self.offset_y = -self.view_height / 2 # want 0,0 as center
        self.scale = 1
        self.start_pan_x = 0
        self.start_pan_y = 0
        self.selected_x = 0
        self.selected_y = 0


    def handle_event(self, event):
        # Exiting
        if event.type == pygame.QUIT:
            self.running = False

        # Add patterns based on mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Add pattern
            if event.button == 1:
                self.add_pattern(self.mouse_pattern, mouse_x, mouse_y)
            # Cycle patterns


    def next_gen(self):
        # Store previous generation
        grid = copy.deepcopy(self.grid)

        # Check number of neighbors for each cell
        for row in range(self.grid_size):
            for col in range(self.grid_size):
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
                    row + i > self.grid_size - 1 or
                    col + j < 0 or
                    col + j > self.grid_size - 1 or
                    (i == 0 and j == 0)): continue
                else:
                    neighbors += grid[row + i][col + j]
        return neighbors
    

    def world_to_screen(self, grid_x, grid_y):
        # Convert world coordinates to screen coordinates
        self.view_width = int((self.grid_x - self.offset_x) * self.scale)
        self.view_height = int((self.grid_y - self.offset_y) * self.scale)


    def screen_to_world(self, screen_x, screen_y):
        # Convert screen coordinates to world coordinates
        self.grid_x = (float(screen_x) / self.scale) + self.offset_x
        self.grid_y = (float(screen_y) / self.scale) + self.offset_y


    def fill_area(self, row, col, width, height, state):
        # Fill area with state-based cells
        for i in range(height):
            for j in range(width):
                self.grid[row + i][col + j] = state


    def add_pattern(self, pattern, row, col):
        pattern_width = len(pattern[0])
        pattern_height = len(pattern)

        # Check if pattern is fully within grid
        if row + pattern_height > self.grid_size or col + pattern_width > self.grid_size:
            return

        # Make sure pattern exists and then add it to grid
        if pattern:
            # Fill background area and one layer border with 0s
            self.fill_area(row, col, pattern_width, pattern_height, 0)
            # Fill pattern area with 1s
            for i in range(pattern_height):
                for j in range(pattern_width):
                    self.grid[row + i][col + j] = pattern[i][j]


    def render(self):
        # Use screen space to draw grid
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                color = BG_COLOR
                if self.grid[row][col] == 1:
                    color = FG_COLOR
                rect = pygame.Rect(col * self.block_w,
                                   row * self.block_h,
                                   self.block_w, self.block_h)
                pygame.draw.rect(self.display_surf, color, rect)
        pygame.display.flip()


    def cleanup(self):
        pygame.quit()


    def run(self):
        while(self.running):
            # Event handling
            for event in pygame.event.get():
                self.handle_event(event)
            self.next_gen()
            self.render()
            self.clock.tick(FRAMERATE)
        self.cleanup()


if __name__ == "__main__":
    game = Game()
    game.run()
