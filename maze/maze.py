import numpy as np
from enum import Enum
from collections import deque
from queue import Queue, PriorityQueue


class Action(Enum):
    """
    Action: [delta_row, delta_col, cost]
    """
    LEFT = (0, -1, 1)
    RIGHT = (0, 1, 1)
    UP = (-1, 0, 1)
    DOWN = (1, 0, 1)

    def __str__(self):
        if self == self.LEFT:  return '<'
        elif self == self.RIGHT: return '>'
        elif self == self.UP: return '^'
        elif self == self.DOWN: return 'v'

    @property
    def cost(self):
        return self.value[2]

    @property
    def delta(self):
        return (self.value[0], self.value[1])


class Maze(object):
    """
    Solving the maze with breath first search (finding the shortest path).

    position: breath first search (partial plan)

    cost: evaulating the path performance
      - node_cost
      - cost = heuristic(node) + node_cost
      - heuristic = sqrt((node[0] - goal[0])^2 + (node[1] - goal[1])**2)
    """


    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal


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


    def heuristic(self, position):
        h = np.sqrt((self.goal[0] - position[0])**2 + (self.goal[1] - position[1])**2)
        return h


    def breath_first_a_start_deque(self):
        path = []
        path_cost = 0

        queue = deque()
        queue.append(self.start)
        visited = []

        branch = {}
        found = False
        
        while len(queue) > 0:
            current_node = queue.popleft()
            if current_node == self.goal:
                print("Found a path.")
                found = True
                break;
            else:
                for x in self.valid_actions(current_node):
                    next_node = (current_node[0] + x.delta[0], current_node[1] + x.delta[1])
                    path_cost += x.cost + self.heuristic(next_node)
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

        return path[::-1], path_cost


    def breath_first_a_start_queue(self):
        path = []
        path_cost = 0

        queue = Queue()
        queue.put(self.start)
        visited = set(self.start)

        branch = {}
        found = False
        while not queue.empty():
            current_node = queue.get()
            if current_node == self.goal:
                print('Found a path.')
                found = True
                break
            else:
                for action in self.valid_actions(current_node):
                    next_node = (current_node[0] + action.delta[0], current_node[1] + action.delta[1])
                    path_cost += action.cost + self.heuristic(next_node)
                    if next_node not in visited:
                        queue.put(next_node)
                        visited.add(next_node)
                        branch[next_node] = (path_cost, current_node, action)

        if found:
            n = self.goal
            path_cost = branch[n][0]
            while branch[n][1] != self.start:
                path.append(branch[n][2])
                n = branch[n][1]
            path.append(branch[n][2])

        return path[::-1], path_cost
       
 
    def breath_first_a_start_priorityqueue(self):
        path = []
        path_cost = 0

        queue = PriorityQueue()
        queue.put((0, self.start))
        visited = set(self.start)

        branch = {}
        found = False
        while not queue.empty():
            current_cost, current_node = queue.get()
            if current_node == self.goal:
                print('Found a path.')
                found = True
                break
            else:
                for action in self.valid_actions(current_node):
                    next_node = (current_node[0] + action.delta[0], current_node[1] + action.delta[1])
                    next_cost = current_cost + action.cost + self.heuristic(next_node)
                    if next_node not in visited:
                        queue.put((next_cost, next_node))
                        visited.add(next_node)
                        branch[next_node] = (next_cost, current_node, action)

        if found:
            n = self.goal
            path_cost = branch[n][0]
            while branch[n][1] != self.start:
                path.append(branch[n][2])
                n = branch[n][1]
            path.append(branch[n][2])

        return path[::-1], path_cost
