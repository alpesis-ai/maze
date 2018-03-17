import numpy as np

from maze import Maze


if __name__ == '__main__':

    grid = np.array([
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 0],
    ])
    start = (0, 0)
    goal = (4, 4)

    maze_t = Maze(grid, start, goal)
 
    path, path_cost = maze_t.breath_first_a_start_deque()
    print("breath_first_a_start_deque: ", path_cost, "\n", maze_t.visualize_path(path))

    path, path_cost = maze_t.breath_first_a_start_queue()
    print("breath_first_a_start_queue: ", path_cost, "\n", maze_t.visualize_path(path))

    path, path_cost = maze_t.breath_first_a_start_priorityqueue()
    print("breath_first_a_start_priorityqueue: ", path_cost, "\n", maze_t.visualize_path(path))
