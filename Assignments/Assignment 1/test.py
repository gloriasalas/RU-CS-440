import heapq
import setup_env
import numpy as np

def main():
    start_state = setup_env.grid_list[0][0]
    open_list = []
    open_list.append(start_state)
    x = heapq.heappop(open_list[0])
    index = zip(*np.where(s == x))
    print(index)
