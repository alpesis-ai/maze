from maze import Maze


if __name__ == '__main__':

    maze_t = Maze() 
    path = maze_t.breadth_first()
    print("breath_first_search:\n", maze_t.visualize_path(path))
    path = maze_t.depth_first()
    print("depth_first_search:\n", maze_t.visualize_path(path))
