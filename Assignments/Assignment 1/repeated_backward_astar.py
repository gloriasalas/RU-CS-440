import heapq
import math
import queue
import setup_env
from time import time

maze = setup_env.grid_list[0]

def compute_path(open_list, closed_list, counter, g_s_goal):
    while(g_s_goal > open_list[0].f):
        node = heapq.heappop(open_list)
        actions_list = node.expand(maze)
        closed_list.append(node)
        for subnode in actions_list:
            if subnode in closed_list:
                continue
            if subnode.search_value < counter:
                subnode.g = float('inf')
                subnode.search_value = counter
            if subnode.g > (node.g + 1):
                subnode.g = node.g + subnode.action_cost
                subnode.parent = node
                if subnode in open_list:
                    open_list.remove(subnode)
                #set h-value for subnode
                subnode.h = abs(subnode.x - 100) + abs(subnode.y - 100) #100 being the x and y coordinates of the goal
                subnode.f = subnode.g + subnode.h
                heapq.heappush(open_list, subnode)
        actions_list = []

def main():
    start_time = time()
    states = []
    counter = 0
    start_state = maze[100][100]
    goal_state = maze[0][0]
    open_list = []
    closed_list = []
    for s in states:
        s.search_value = 0
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
            if (square.blocked):
                square.action_cost = float('inf')
                break
            start_state = square
        setup_env.draw_grid(maze[0])
    print("I reached the target.")
    return
        
if __name__ == "__main__":
    main()
        

        
        
