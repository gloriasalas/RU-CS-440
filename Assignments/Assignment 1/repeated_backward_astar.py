import heapq
import math
import queue
import setup_env
from time import time

def compute_path(open_list, closed_list, counter, g_s_goal):
    saw_end = False
    while(len(open_list) != 0 and g_s_goal > open_list[0].f and not saw_end):
        node = heapq.heappop(open_list)
        actions_list = node.expand(maze)
        closed_list.append(node)
        for subnode in actions_list:
            if subnode in closed_list:
                continue
            if subnode.search_value < counter:
                subnode.g = float('inf')
                subnode.search_value = counter
            if subnode.g > (node.g + subnode.action_cost):
                subnode.g = node.g + subnode.action_cost
                subnode.parent = node
                subnode.h = subnode.x + subnode.y #setup_env.max_index being the x and y coordinates of the goal
                subnode.f = subnode.g + subnode.h
                heapq.heappush(open_list, subnode)
                if subnode.position == (0, 0):
                    saw_end = True
                break

def main(maze):
    start_time = time()
    counter = 0
    start_state = maze[setup_env.max_index][setup_env.max_index]
    goal_state = maze[0][0]
    open_list = []
    closed_list = []
    while start_state != goal_state:
        counter += 1
        start_state.g = 0
        start_state.search_value = counter
        goal_state.g = float('inf')
        goal_state.search_value = counter
        open_list = []
        closed_list = []
        start_state.f = start_state.g + start_state.h
        heapq.heappush(open_list, start_state)
        compute_path(open_list, closed_list, counter, goal_state.g)
        if (open_list == []):
            print("I cannot reach the target.")
            return
        #follow tree pointers from s_goal to s_start then move the agent along the resulting path
        #from s_start to s_goal until it reaches s_goal or one or more action costs on the path increase;
        #set s_start to the current state of the agent (if it moved);
        #update the increased action costs (if any);
        path = []
        tree_ptr = goal_state
        while tree_ptr != start_state:
            path.append(tree_ptr)
            tree_ptr = tree_ptr.parent
        path.append(start_state)
        # path.reverse()
        for square in path:
            print(square.x, square.y)
            if (square.blocked):
                square.action_cost = float('inf')
                start_state = square.parent
                break
            start_state = square
    print("I reached the target.")
    return

if __name__ == "__main__":
    maze = ([[setup_env.Square(x, y, False, False) for x in range(setup_env.dimension)] for y in range(setup_env.dimension)])
    maze[0][0].is_agent = True
    maze[2][0].blocked = True
    maze[3][2].blocked = True
    setup_env.draw_grid(maze)
    
    main(maze)
        

        
        
