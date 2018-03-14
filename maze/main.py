from maze import Maze


if __name__ == '__main__':

    maze_t = Maze() 
    path = maze_t.breadth_first()
    print maze_t.visualize_path(path)
