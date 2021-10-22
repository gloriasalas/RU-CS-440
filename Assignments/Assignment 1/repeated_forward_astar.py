import heapq
import setup_env

maze = setup_env.grid_list[0]

def return_path(current_node, maze):
    path = []
    result = [[-1 for i in range(101)] for j in range(101)]
    curr = current_node
    while curr is not None:
        path.append(curr.position)
        curr = curr.parent

    path = path[::-1]
    start_value = 0
    for i in range(len(path)):
        result[path[i][0]][path[i][1]] = start_value
        start_value += 1
    return result

def search(maze, cost, start, end):
    start_node = setup_env.grid_list[0][0]
    start_node.g = start_node.h = start_node.f = 0
    end_node = setup_env.grid_list[100][100]
    end_node.g = end_node.h = end_node.f = 0

    yet_to_visit_list = []
    visited_list = []
    yet_to_visit_list.append(start_node)

    outer_iterations = 0
    max_iterations = (len(maze) // 2) ** 10
    
    move = [[-1, 0], #up
            [0, -1], #left
            [1, 0],  #down
            [0, 1]]  #right

    while len(yet_to_visit_list) > 0:
        outer_iterations += 1
        curr = yet_to_visit_list[0]
        curr_index = 0
        for index, item in enumerate(yet_to_visit_list):
            if item.f < curr.f:
                curr = item
                curr_index = index

        if outer_iterations > 10000:
            print("too many iterations")
            return return_path(curr, maze)
        
        yet_to_visit_list.pop(curr_index)
        visited_list.append(curr)

        if curr == end_node:
            return return_path(curr, maze)

def compute_path(open_list, closed_list, counter, g_s_goal):
    action_list = []
    while(g_s_goal > open_list[0].f):
        ss = heapq.heappop(open_list[0])
        if ss in closed_list:
            return
        up = maze[ss.x-1][ss.y]
        left = maze[ss.x][ss.y-1]
        down = maze[ss.x+1][ss.y]
        right = maze[ss.x][ss.x+1]
        action_list.append(up)
        action_list.append(left)
        action_list.append(down)
        action_list.append(right)
        closed_list.append(ss) #may need to check if current element is already in closed list
        for a in action_list:
            if a in closed_list:
                continue
            if a.search_value < counter:
                a.g = float('inf')
                a.search_value = counter
            if a.g > (ss.g + 1):
                a.g = ss.g + 1
                ss.parent = a
                if a in open_list:
                    open_list.remove(a)
                a.f = a.g + a.h
                heapq.heappush(open_list, a)

def main():
    states = []
    counter = 0
    start_state = setup_env.grid_list[0][0]
    goal_state = setup_env.grid_list[100][100]
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
        open_list = closed_list = []
        start_state.f = start_state.g + start_state.h
        heapq.heappush(open_list, start_state)
        compute_path(open_list, closed_list, counter, goal_state.g)
        if (open_list == []):
            print("I cannot reach the target.")
            return
        #follow tree pointers from s_goal to s_start then move the agent along the resulting path
        #from s_start to s_goal until it reaches s_goal or one or more action costs on the path
        #increase;
        #set s_start to the current state of the agent (if it moved);
        #update the increased action costs (if any);
    print("I reached the target.")
    return
        
        
        

        
        