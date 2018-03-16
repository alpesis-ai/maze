import numpy as np
from enum import Enum
from collections import deque


class Action(Enum):

    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)

    def __str__(self):
        if self == self.LEFT:  return '<'
        elif self == self.RIGHT: return '>'
        elif self == self.UP: return '^'
        elif self == self.DOWN: return 'v'


class Maze(object):

    def __init__(self):
        self.grid = np.array([
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 0],
        ])

        self.start = (0, 0)
        self.goal = (4, 4)


    def valid_actions(self, current_node):
        """
        Returns a list of valid actions given a grid and current node.
        """
        n, m = self.grid.shape[0] - 1, self.grid.shape[1] - 1
        x, y = current_node
        valid = [Action.UP, Action.LEFT, Action.RIGHT, Action.DOWN]

        # check if the node if off the grid or it is an obstacle
        if (x - 1 < 0) or (self.grid[x - 1, y] == 1): valid.remove(Action.UP)
        if (x + 1 > n) or (self.grid[x + 1, y] == 1): valid.remove(Action.DOWN)
        if (y - 1 < 0) or (self.grid[x, y - 1] == 1): valid.remove(Action.LEFT)
        if (y + 1 > m) or (self.grid[x, y + 1] == 1): valid.remove(Action.RIGHT)

        return valid


    def visualize_path(self, path):
        """
        Representation:
            - 'S' -> start
            - 'G' -> goal
            - 'O' -> obstacle
            - ' ' -> empty
        """
        # define a grid of string characters for visualization
        solution = np.zeros(np.shape(self.grid), dtype=np.str)
        solution[:] = ' '
        solution[self.grid[:] == 1] = 'O'

        position = self.start
        for x in path:
            solution[position[0], position[1]] = str(x)
            position = (position[0] + x.value[0], position[1] + x.value[1])

        solution[position[0], position[1]] = 'G'
        solution[self.start[0], self.start[1]] = 'S'
        return solution


    def breadth_first(self):
        path = []
        queue = deque()
        visited = []

        branch = {}
        found = False

        queue.append(self.start)
        while len(queue) > 0:
            current_node = queue.popleft()
            if current_node == self.goal:
                print("Found a path.")
                found = True
                break;
            else:
                for x in self.valid_actions(current_node):
                    delta = x.value
                    next_node = (current_node[0] + delta[0], current_node[1] + delta[1])
                    if next_node not in visited:
                        queue.append(next_node)
                        visited.append(current_node)
                        branch[next_node] = (current_node, x)
        if found:
            n = self.goal
            while branch[n][0] != self.start:
                path.append(branch[n][1])
                n = branch[n][0]
            path.append(branch[n][1])

        return path[::-1]
