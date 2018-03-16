from maze import Maze


if __name__ == '__main__':

    maze_t = Maze()
 
    path, path_cost = maze_t.breath_first_deque()
    print("breath_first_deque: ", path_cost, "\n", maze_t.visualize_path(path))

    path, path_cost = maze_t.breath_first_queue()
    print("breath_first_queue: ", path_cost, "\n", maze_t.visualize_path(path))

    path, path_cost = maze_t.breath_first_priority_queue()
    print("breath_first_priority_queue: ", path_cost, "\n", maze_t.visualize_path(path))
