"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id, connections=None):
        """
        Add a vertex to the graph.
        """
        if connections:
            # check that all connection verts are valid
            ok = self.validate_edges(connections)
            if not ok:
                raise ValueError(
                    f'Invalid connection. Node {c} does not exist in this graph.')
            self.vertices[vertex_id] = connections
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, vert, new_edge):
        """
        Add a directed edge to the graph.
        """
        # check vertice
        if vert not in self.vertices:
            raise ValueError(f'Invalid node {vert}')
        # check new edge
        if new_edge not in self.vertices:
            raise ValueError(f'Invalid edge {new_edge}')
        self.vertices[vert].add(new_edge)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        raise ValueError('Vertex does not exist')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #  create queue
        will_process = deque()
        # enqueue start vertex
        will_process.append(starting_vertex)
        # create set to store visited vertices
        visited = set()
        # while queue is not empty
        while len(will_process) > 0:
            # dequeue first vert
            current = will_process.popleft()
            # print vertex when it is visited
            print(current)
            # mark as visited
            visited.add(current)
            # enqueue unvisited
            for n in self.vertices[current]:
                if n not in visited:
                    will_process.append(n)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #  create stack
        will_process = deque()
        # push start vertex to stack
        will_process.append(starting_vertex)
        # create set to store visited vertices
        visited = set()
        # while stack is not empty
        while len(will_process) > 0:
            # dequeue first vert
            current = will_process.pop()
            if current not in visited:
                # print current vertex
                print(current)
                # mark as visited
                visited.add(current)
                # enque unvisited neighbors
                for n in self.vertices[current]:
                    if n not in visited:
                        will_process.append(n)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
#  create queue
        # enqueue A PATH to start vertex
        # create set to store visited vertices
        # while queue is not empty
        # dequeue first vert
        # get the vertex from the end of the path
        # check if visited
        # if not visited
        # check if it is the destination
        # if so ,return vertex
        # mark as visited
        # enque a path to all of its neighbors
        # enque the copy

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

    def validate_edges(self, connections):
        ok = True
        for c in connections:
            if not self.vertices.get(c):
                ok = False
                break
        return ok


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
