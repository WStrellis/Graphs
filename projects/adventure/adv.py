from room import Room
from player import Player
from world import World

from maze_traveler import MazeTraveler

import random
from ast import literal_eval
import pprint

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "./projects/adventure/maps/test_line.txt"
# map_file = "./projects/adventure/maps/test_cross.txt"
# map_file = "./projects/adventure/maps/test_loop.txt"
# map_file = "./projects/adventure/maps/test_loop_fork.txt"
map_file = "./projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

# show room data structure
pp = pprint.PrettyPrinter(indent=4, width=79)
# pp.pprint(world.starting_room.get_exits())

# for [k, v] in world.rooms.items():
#     pp.pprint(f'key:{k}, room exits: {v.get_exits()}, room id: {v.id}')

# pp.pprint(str(world.rooms[1].get_room_in_direction('s')))

player = Player(world.starting_room)

# Fill this out with directions to walk
traveler = MazeTraveler(world)
# pp.pprint(traveler.adj_list)

# traversal_path = traveler.traverse_maze()
result = traveler.traverse_maze()


# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

if len(result[1]) == len(room_graph):
    print(
        f"TESTS PASSED: {len(result[0])} moves, {len(result[1])} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(result[1])} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# # player.current_room.print_room_description(player)
# # while True:
# #     cmds = input("-> ").lower().split(" ")
# #     if cmds[0] in ["n", "s", "e", "w"]:
# #         player.travel(cmds[0], True)
# #     elif cmds[0] == "q":
# #         break
# #     else:
# #         print("I did not understand that command.")
