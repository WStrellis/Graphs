from collections import deque
from operator import itemgetter


class MazeTraveler():
    def __init__(self, world):
        self.world = world
        self.adj_list = {}
        # the path traveled
        self.path = []
        # count number of rooms fully explored( no rooms with'?' in adj_list)
        self.fully_explored = 0

        # initialize adj_list
        for room in world.rooms:
            self.adj_list[room] = {'n': '?', 's': '?', 'e': '?', 'w': '?'}

    def traverse_maze(self):
        """Uses a combination of DFT and BFS to find all room in a maze

        Returns:
            :list -- a list of the steps take to traverse the entire map
        """
        self.dft()

        return self.path

    def dft(self):
        """Go as far as possible. when a dead end has been reached use BFS to go back to last room with an unsearched exit.
        """
        start = self.world.starting_room
        stak = [start]

        while len(stak):
            current = stak.pop()
            # get the next room and the direction it is in
            result = self.get_undiscovered(current)
            neighbor = result['neighbor']
            direction = result['direction']

            if neighbor:
                # update self.adj_list for current and neighbor
                self.update_adj_list(current, neighbor, direction)
                # add neighbor to stack
                stak.append(neighbor)
                # add direction to path
                self.path.append(direction)
            else:
                # use BFS search to find closest neighbor with undiscovered exit
                next_room = self.bfs(current)
                # add the room returned from BFS to the stack
                if next_room is not None:
                    stak.append(next_room)

    def bfs(self, start_room):
        """find the shortest path to a room with an undiscovered neighbor

        Arguments:
            start_room : Room instance

        Returns:
            room : Room instance
        """
        # create queue to store path
        q = deque()
        # create set to store visited rooms
        visited = set()
        # init q
        q.append({'path': [], 'rooms': [start_room]})

        while len(q):
            current_item = q.pop()
            directions_traveled = current_item['path']
            rooms_traveled = current_item['rooms']
            # get last room in rooms_traveled
            current_room = rooms_traveled[-1]
            # check if room has any '?' in self.adj_list
            has_unexplored = any(
                [v for v in self.adj_list[current_room.id].values() if v == '?'])
            if has_unexplored:
                # add directions_traveled to self.path
                self.path.extend(directions_traveled)
                # return found room
                return current_room
            else:
                # check if room in visted
                if current_room not in visited:
                    # add room to visited
                    visited.add(current_room)
                # enqueue path to all neighbor rooms that have not been visited
                # get neighbor in each direction
                for d in ['n', 's', 'e', 'w']:

                    result = current_room.get_room_in_direction(d)
                    neighbor = result['neighbor']
                    direction = result['direction']
                    if neighbor not in visited and neighbor is not None:
                        q.append(
                            {'path': [*directions_traveled, d], 'rooms': [*rooms_traveled, neighbor]})

    def get_undiscovered(self, room):
        """ used to find undisovered rooms

        Arguments:
            room : Room instance

        Returns:
            dictionary
               -- "direction": str
               --  "room": Room  instance or None
                    """
        neighbor = None
        direction = None
        # look in self.adj_list for the room and see if it has any '?'
        for [d, n] in self.adj_list[room.id].items():
            # for each direction with a '?', see if room has a neighbor in that direction
            if n == '?':
                found = room.get_room_in_direction(d)
                # if it does, update values of the neighbor and the direction of neighbor
                if found['neighbor'] is None:
                    self.update_adj_list(room, None, d)
                else:
                    neighbor = found['neighbor']
                    direction = d

        # if no neighbors found
        # increment self.fully_explored
        if neighbor == None:
            self.fully_explored += 1

        return {'direction': direction, 'neighbor': neighbor}

    def opposite_direction(self, direction):
        """ 
        return the opposite direction of the input direction
        """
        opposites = {
            'n': 's',
            's': 'n',
            'w': 'e',
            'e': 'w',
        }
        return opposites[direction]

    def update_adj_list(self, current, found, direction):
        """when a room is found update the connections in the adjacency list for the current room and the found room
        """
        # replace '?' with None if there is not a room in the specified direction
        if found is not None:
            self.adj_list[current.id][direction] = found.id
            self.adj_list[found.id][self.opposite_direction(
                direction)] = current.id
        else:
            self.adj_list[current.id][direction] = None
