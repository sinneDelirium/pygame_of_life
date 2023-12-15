import copy


ITERATIONS = 4
SIZE = 10
BLINKER = [[1],
           [1],
           [1]
           ]


class Game:
    def __init__(self):
        self.grid_width = self.grid_height = SIZE
        self.grid = [[0 for x in range(self.grid_width)] for y in range(self.grid_height)]
        self.add_pattern(0, 4, 4)


    def next_gen(self):
        # Store previous generation
        grid = copy.deepcopy(self.grid)

        # Check number of neighbors for each cell
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                neighbors = self.count_neighbors(row, col, grid)
                alive = grid[row][col]
                # Depending on neighbors, follow rules of life
                if (alive == 1 and neighbors < 2):
                    self.grid[row][col] = 0
                elif (alive == 1 and neighbors > 3):
                    self.grid[row][col] = 0
                elif (alive == 0 and neighbors == 3):
                    self.grid[row][col] = 1
                else:
                    self.grid[row][col] = grid[row][col]


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
            for i in range(len(BLINKER)):
                for j in range(len(BLINKER[i])):
                    self.grid[row + i][col + j] = BLINKER[i][j]


    def render(self):
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if (self.grid[row][col] == 1):
                    print("1", end="")
                elif (self.grid[row][col] == 1 and col == self.grid_width - 1):
                    print("1")
                elif (self.grid[row][col] == 0 and col == self.grid_width - 1):
                    print("0")
                else:
                    print("0", end="")


    def execute(self):
        iter = 0
        print("Iteration: " + str(iter))
        self.render()
        iter += 1
        while (iter < ITERATIONS + 1):
            print("Iteration: " + str(iter))
            self.next_gen()
            self.render()
            iter += 1


if __name__ == "__main__":
    game = Game()
    game.execute()
