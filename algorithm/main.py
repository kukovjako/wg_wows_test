import random
from collections import deque


class MapGenerator:
    #  class generates map, but pathfinding logic is not finished.

    def __init__(self, columns, rows):
        self.width = columns
        self.length = rows

    @staticmethod
    def rand_choice(range_: int):
        return random.choice(range(0, range_))

    def generate_map(self):
        land_counter = 0
        field = [[0 for w in range(self.width)] for l in range(self.length)]
        # 30% of all cells in massive rounded
        land_limit = int(((self.width * self.length) / 30 * 10))
        while land_counter <= land_limit:
            row_num = self.rand_choice(self.width)
            cell = self.rand_choice(self.length)
            field[row_num][cell] = 1  # setting land
            land_counter += 1

        for row in field:
            print(" ".join(list(map(str, row))))
        return field

    def get_next_nodes(self, x, y, field):
        check_next_node = (
            lambda x, y: True
            if 0 <= x < self.width and 0 <= y < self.length and not field[y][x]
            else False
        )
        ways = [-1, 0], [0, -1], [1, 0], [0, 1]
        return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]

    def bfs(self, graph, start, goal):
        queue = deque([start])
        visited = {start: None}

        while queue:
            cur_node = queue.popleft()
            if cur_node == goal:
                break

            next_nodes = graph[cur_node]
            for next_node in next_nodes:
                if next_node not in visited:
                    queue.append(next_node)
                    visited[next_node] = cur_node
        return queue, visited

    def find_path(self, start: tuple, goal: tuple):
        start = start if start else (0, 0)
        goal = goal if start else (0, 0)
        field = self.generate_map()
        queue = deque([start])
        visited = {start: None}

        graph = {}
        for y, row in enumerate(field):
            for x, col in enumerate(row):
                if not col:
                    graph[(x, y)] = graph.get((x, y), []) + self.get_next_nodes(
                        x, y, field
                    )

        queue, visited = self.bfs(graph, start, goal)

        # draw path
        path_head, path_segment = goal, goal
        while path_segment and path_segment in visited:
            pass

        # not working as is


if __name__ == "__main__":
    map_gen = MapGenerator(10, 10)
    map_gen.generate_map()
