import random

class Square:
    def __init__(self, visited, blocked, isAgent):
        self.visited = visited
        self.blocked = blocked
        self.isAgent = False

# class Grid(Square):
#     def __init__(self):
#         grid = [[Square(False, False) for x in range(101)] for y in range(101)]

grid = [[Square(False, False, False) for x in range(101)] for y in range(101)]

#iterate through grid_list and assign all squares as blocked or unblocked with a 3:7 ratio

grid_list = []
for i in range(50):
    grid_list.append(grid)

stack = []

for grid in grid_list:
    starting_square = grid[0][0]
    ending_square = grid[100][100]
    starting_square.visited = True
    starting_square.isAgent = True
    for i in range(101):
        for square in grid[i]:
            if not(grid[i].index(square) == 0 and i == 0) and not(grid[i].index(square) == 101 and i == 101):
                n = random.randrange(1, 100)
                if n > 70:
                    square.blocked = True
                # print(square.blocked)

def draw_grid(grid):
    for i in range(101):
        for square in grid[i]:
            if square.isAgent:
                print("A")
            elif grid[i].index(square) == 101 and i == 101:
                print("T")
            elif square.blocked == True:
                print("X")
            elif square.blocked == False:
                print(" ")
            if grid[i].index(square) == 101:
                print("\n")

draw_grid(grid_list[0])

