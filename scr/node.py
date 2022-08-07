from abc import ABC, abstractmethod


class Node(ABC):
    """
    __str__ : return data of node
    __eq__: check if nodes are equal
    is_solution: check if node is solution or not
    extend_node:

    """

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def is_solution(self, state):
        pass

    @abstractmethod
    def extend_node(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass


class MazeNode(Node):

    def __init__(self, graph, value):
        self.graph = graph
        self.value = value
        self.parent = None

    def __eq__(self, other):
        if isinstance(other, MazeNode):
            return self.value == other.value
        return self.value == other

    def is_solution(self, final_state):
        return self.value == final_state

    def __str__(self):
        total_path = self._find_path()
        path = ' -> '.join(total_path)
        return path

    def total_way(self):
        total_path = self._find_path()
        return len(total_path)

    def extend_node(self):
        children = [MazeNode(self.graph, child) for child in self.graph[self.value]]
        for child in children:
            child.parent = self
        return children

    def _find_path(self):
        path = []
        current_node = self
        while current_node.parent is not None:
            path.insert(0, current_node.value)
            current_node = current_node.parent
        path.insert(0, current_node.value)
        return path
