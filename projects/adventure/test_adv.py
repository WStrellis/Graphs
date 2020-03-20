from room import Room
from player import Player
from world import World
from maze_traveler import MazeTraveler

import unittest
import random
from ast import literal_eval
import pprint


# You may uncomment the smaller graphs for development and testing purposes.
line_map = "./projects/adventure/maps/test_line.txt"
cross_map = "./projects/adventure/maps/test_cross.txt"
loop_map = "./projects/adventure/maps/test_loop.txt"
# map_file = "./projects/adventure/maps/test_loop_fork.txt"
# map_file = "./projects/adventure/maps/main_maze.txt"


class Test(unittest.TestCase):
    def setUp(self):
        # line map
        self.line_world = World()
        self.line_map = literal_eval(open(line_map, "r").read())

    def test_get_room_in_direction(self):
        world = World()
        world.load_graph(self.line_map)
        room0 = world.rooms[0]
        room1 = world.rooms[1]

        self.assertEqual(room0.get_room_in_direction(
            'n'), {'direction': 'n', 'neighbor': room1})

        self.assertEqual(room0.get_room_in_direction(
            's'), {'direction': 's', 'neighbor': None})

    def test_adjacency_list(self):
        world = World()
        world.load_graph(self.line_map)

        traveler = MazeTraveler(world)

        self.assertEqual(traveler.adj_list, {0: {'n': '?', 's': '?', 'e': '?', 'w': '?', }, 1: {'n': '?', 's': '?', 'e': '?', 'w': '?', }, 2: {'n': '?', 's': '?', 'e': '?', 'w': '?', }
                                             })

    def test_line(self):
        world = World()
        # Loads the map into a dictionary
        world.load_graph(self.line_map)

        traveler = MazeTraveler(world)
        traversal_path = traveler.traverse_maze()

        self.assertEqual(traversal_path, ['n', 'n'])
