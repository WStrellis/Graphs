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

    def dft_recursive(self, vertex,  visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # initialize set to track visited
        if visited == None:
            visited = set()

        # if current vertex not in visited, add to visited
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            # call on neighbors
            for v in self.vertices[vertex]:
                self.dft_recursive(v, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #  create queue
        will_process = deque()
        # init queue
        will_process.append([starting_vertex])
        # create set to store visited vertices
        visited = set()
        # while queue is not empty
        while len(will_process):
            # dequeue first vert
            current_path = will_process.popleft()
            # get the vertex from the end of the path
            current_vert = current_path[-1]

            # check if it is the destination
            if current_vert == destination_vertex:
                return current_path

            # check if visited
            if current_vert not in visited:
                # mark as visited
                visited.add(current_vert)
                # enque a path to all of its neighbors
                for v in self.vertices[current_vert]:
                    copy = current_path.copy()
                    will_process.append([*copy, v])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create stack
        will_process = [[starting_vertex]]
        # track visited
        visited = set()
        while len(will_process):
            current_path = will_process.pop()
            current_vert = current_path[-1]
            if current_vert == destination_vertex:
                return current_path
            if current_vert not in visited:
                visited.add(current_vert)

                for v in self.vertices[current_vert]:
                    copy = current_path.copy()
                    will_process.append([*copy, v])

    def dfs_recursive(self, starting_vertex, target, path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # create stack
        if path == None:
            path = []
        # track visited
        if visited == None:
            visited = set()

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)

            if starting_vertex == target:
                return path_copy

            for n in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(
                    n,  target, path_copy, visited)
                if new_path is not None:
                    return new_path

        return None

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
    # print(graph.vertices)

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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

"""         # create stack
        if will_process == None:
            will_process = [[starting_vertex]]
        # track visited
        if visited == None:
            visited = set()

        current_path = will_process.pop()
        current_vert = current_path[-1]

        if current_vert == target:
            return current_path
        else:
            if current_vert not in visited:
                visited.add(current_vert)

            for v in self.vertices[current_vert]:
                if v not in visited:
                    will_process.append(current_path + [v])
                    self.dfs_recursive(current_path, target,
                                       will_process, visited)

 """
