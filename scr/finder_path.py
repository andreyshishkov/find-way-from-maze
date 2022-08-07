from scr.node import MazeNode


class BFS:

    def __init__(self, start: MazeNode, final: str):
        self.start_state = start
        self.final_state = final
        self.checked_nodes = []
        self.path = []
        self.number_of_steps = 0
        self.frontier = [self.start_state]

    def insert_to_frontier(self, node):
        self.frontier.append(node)

    def remove_from_frontier(self):
        first_node = self.frontier.pop(0)
        self.checked_nodes.append(first_node)
        return first_node

    def frontier_is_empty(self):
        if len(self.frontier) == 0:
            return True
        return False

    def __call__(self):
        while True:

            if self.frontier_is_empty():
                print('No solution !')
                return 0, 'No solution'

            self.number_of_steps += 1

            selected_node = self.remove_from_frontier()

            if selected_node.is_solution(self.final_state):
                print('Found solution')
                return selected_node.total_way() - 1, str(selected_node)

            new_nodes = selected_node.extend_node()
            if len(new_nodes):
                for node in new_nodes:
                    if node not in self.frontier and node not in self.checked_nodes:
                        self.insert_to_frontier(node)


if __name__ == '__main__':
    graph = {
        "A": ['S'],
        "B": ['C', 'D', 'S'],
        "C": ['B', 'J'],
        "D": ['B', 'G', 'S'],
        "E": ['G', 'S'],
        "F": ['G', 'H'],
        "G": ['D', 'E', 'F', 'H', 'J'],
        "H": ['F', 'G', 'I'],
        "I": ['H', 'J'],
        "J": ['C', 'G', 'I'],
        "S": ['A', 'B', 'D', 'E']
    }

    mazes = MazeNode(graph, "S")
    bfs = BFS(mazes, "I")
    print(bfs())
