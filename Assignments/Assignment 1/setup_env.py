import random

class Square:
    def __init__(self, x, y, visited, blocked, parent=None, position=None):
        self.x = x
        self.y = y
        self.visited = visited
        self.blocked = blocked
        self.is_agent = False
        self.parent = parent
        self.position = position
        self.g = float('inf')
        self.h = 0
        self.f = 0
        self.search_value = 0

    def __eq__(self, other):
        return self.position == other.position

grid_list = [] #list of 50 grids
for i in range(50):
    grid_list.append([[Square(x, y, False, False) for x in range(101)] for y in range(101)])

for grid in grid_list:
    starting_square = grid[0][0]
    starting_square.visited = True
    starting_square.is_agent = True
    for i in range(101):
        for j in range(101):
            if not(i == 0 and j == 0) and not(i == 100 and j == 100):
                n = random.randint(1, 10)
                if n > 7:
                    grid[i][j].blocked = True
                # print(grid[i][j].blocked)

def draw_grid(grid):
    for i in range(101):
        grid_string = ""
        for square in grid[i]:
            if square.is_agent:
                grid_string += "A"
            elif grid[i].index(square) == 100 and i == 100:
                grid_string += "T"
            elif square.blocked == True:
                grid_string += "X"
            elif square.blocked == False:
                grid_string += "_"
            if grid[i].index(square) == 100:
                grid_string += "\n"
        print(grid_string)

draw_grid(grid_list[0])

#set variable for gridsize (optional)

