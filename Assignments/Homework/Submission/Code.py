import random

class Square:
    def __init__(self, visited, blocked):
        self.visited = visited
        self.blocked = blocked
        self.isAgent = False
        # print(self.blocked)

# class Grid(Square):
#     def __init__(self):
#         grid = [[Square(False, False) for x in range(101)] for y in range(101)]

#iterate through grid_list and assign all squares as blocked or unblocked with a 3:7 ratio

grid_list = [] #list of 50 grids
for i in range(50):
    grid_list.append([[Square(False, False) for x in range(10)] for y in range(10)])

# stack = []

for grid in grid_list:
    starting_square = grid[0][0]
    starting_square.visited = True
    starting_square.isAgent = True
    for i in range(10):
        for j in range(10):
            if not(i == 0 and j == 0) and not(i == 9 and j == 9):
                n = random.randrange(1, 10)
                # print(grid[i][j].blocked)
                if n > 7:
                    grid[i][j].blocked = True
                print(grid[i][j].blocked)

def draw_grid(grid):
    for i in range(10):
        empty_string = ""
        for square in grid[i]:
            if square.isAgent:
                # print("A")
                empty_string += "A"
            elif grid[i].index(square) == 9 and i == 9:
                empty_string += "T"
            elif square.blocked == True:
                # print("X")
                empty_string += "X"
            elif square.blocked == False:
                # print(" ")
                empty_string += " "
        if grid[i].index(square) == 9:
            # print("\n")
            empty_string += "\n"
        print(empty_string)

draw_grid(grid_list[0])

#set variable for gridsize

