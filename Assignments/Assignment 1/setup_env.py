import random

dimension = 5
max_index = dimension - 1
num_grids = 50

class Square:
    def __init__(self, x, y, visited, blocked, parent=None):
        self.x = x
        self.y = y
        self.visited = visited
        self.blocked = blocked
        self.is_agent = False
        self.parent = parent
        self.position = (x, y)
        self.g = 0
        self.h = 0
        self.f = 0
        self.search_value = 0
        self.action_cost = 1

    # def __eq__(self, other):
    #     return self.position == other.position
    
    def __lt__(self, other):
        return self.f < other.f

    def expand(self, maze):
        actions_list = []
        if self.x+1 < dimension:
            actions_list.append(maze[self.x+1][self.y])
        if self.x-1 >= 0:
            actions_list.append(maze[self.x-1][self.y])
        if self.y+1 < dimension:
            actions_list.append(maze[self.x][self.y+1])
        if self.y-1 >= 0:
            actions_list.append(maze[self.x][self.y-1])
        return actions_list

grid_list = [] #list of 50 grids
for i in range(num_grids):
    grid_list.append([[Square(x, y, False, False) for x in range(dimension)] for y in range(dimension)])

for grid in grid_list:
    starting_square = grid[0][0]
    starting_square.visited = True
    starting_square.is_agent = True
    for i in range(dimension):
        for j in range(dimension):
            if not(i == 0 and j == 0) and not(i == max_index and j == max_index):
                n = random.randint(1, 10)
                if n > 7:
                    grid[i][j].blocked = True
                # print(grid[i][j].blocked)

def draw_grid(grid):
    for i in range(dimension):
        grid_string = ""
        for square in grid[i]:
            if square.is_agent:
                grid_string += "A"
            elif grid[i].index(square) == max_index and i == max_index:
                grid_string += "T"
            elif square.blocked == True:
                grid_string += "X"
            elif square.blocked == False:
                grid_string += "_"
            if grid[i].index(square) == max_index:
                grid_string += "\n"
        print(grid_string)

# draw_grid(grid_list[0])

