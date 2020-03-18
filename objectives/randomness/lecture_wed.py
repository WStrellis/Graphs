"""Write a function that takes a 2D binary array and returns the number of  islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4
"""


def island_counter(matrix):
    # create visited matrix
    visited = []

    # create matrix to track visited
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    # island counter
    island_count = 0

    # for all nodes:
    for col in range(len(matrix)):
        for row in range(len(matrix)):
            # if node is not visited:
        if not visited[row][col]:
            # if node is a one that has not been visited:
            if matrix[row][col] == 1:
                # mark as visited
                # increment visited count
                visited = dft(row, col, matrix, visted)
                # traverse all nodes, marking as visited
                island_count += 1
    return island_count


def dft(row, col, matrix, visited):
    # do a dtf traversal
    #  create stack
    s = []
    # push start vertex to stack
    s.append(starting_vertex)
    # create set to store visited vertices
    # while stack is not empty
    while len(s):
        # dequeue first vert
        current = s.pop()
        row = visited[0]
        col = visited[1]

        if not visited[row][col]:
            visited[row][col] = True
            for n in get_neighbors(row, col, matrix):
                s.append(neighbor)
    return visted


def get_neighbors(row,  col, matrix):
    neighbors = []
    # check north
    if row > 0 and matrix[row-1][col] == 1:
        neighbors.append((row-1, col))
    # check south
    if row < len(matrix) - 1 and matrix[row+1][col] == 1:
        neighbors.append((row+1, col))
    # check east
    if col < len(matrix[0]) - 1 and matrix[row][col+1] == 1:
        neighbors.append((row, col+1))
    # check west
    if col > 0 and matrix[row][col-1] == 1:
        neighbors.append((row, col-1))
    return neighbors


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0]]
​
islands2 = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]


if __name__ == '__main__':

    print(island_counter(islands))
    print(island_counter(islands2))
