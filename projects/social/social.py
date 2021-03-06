from random import shuffle, randint
from collections import deque
import pprint
import time


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f'User_{i + 1}')

        # Calculate all possible friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # shuffle list of friendships
        shuffle(possible_friendships)

        # calculate total number of friendships to use and add to self
        # create n friendships where n = avg_friendships * num_users  // 2
        # avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # check if user exists
        if not self.users.get(user_id):
            raise ValueError(f'Error: No such user {user_id}')

        visited = {}  # Note that this is a dictionary, not a set
        # create queue to store unprocessed paths
        q = deque()
        # initialize q
        q.append([user_id])

        # while queue is not empty:
        while len(q):
            # get first item in q
            path = q.popleft()
            user = path[-1]
            # check if user has been visited
            if not visited.get(user):
                # if not, add user as key to visited with value as path
                visited[user] = path
                # equeue a path to each neighbor
                for friend in self.friendships[user]:
                    path_copy = path.copy()
                    q.append([*path_copy, friend])

        return visited

    def populate_graph_linear(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # Add users
        # Write a for loop that calls create user the right amount of times
        for i in range(num_users):
            self.add_user(f"User {i+1}")
        target_friendships = num_users * avg_friendships
        total_friendships = 0
        collisions = 0
        while total_friendships < target_friendships:
            # Pick a random user
            user_id = randint(1, num_users)
            # Pick another random user
            friend_id = randint(1, num_users)
            # Try to create the friendship
            if self.add_friendship(user_id, friend_id):
                # If it works, increment a counter
                total_friendships += 2
            else:
                # If not, try again
                collisions += 1
        print(f"NUM COLLISIONS: {collisions}")


def percent_of_users(num_users, user, user_connections):
    """given a number of users in a network, a specific user, and the user's complete network, return the percentage of other users in that user's social network

    Arguments:
        num_users: int
        user: int
        social_connections: obj
    """
    # count all friends including user's extended network
    friends = set()
    for [_user, _friends] in user_connections.items():
        friends.update(_friends)
    # remove user from list of extended network friends
    friends.remove(user)
    # divide num_users by friend
    return f'{len(friends) / num_users :.2%}'


if __name__ == '__main__':
    # pp = pprint.PrettyPrinter(indent=4, width=79)
    # sg = SocialGraph()
    # sg.populate_graph(10, 2)
    # pp.pprint(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # pp.pprint(connections)
    # print(percent_of_users(10, 1, connections))

    # sg2 = SocialGraph()
    # sg2.populate_graph(1000, 5)
    # print(sg2.friendships)
    # connections2 = sg2.get_all_social_paths(1)
    # print(connections2)
    # print(percent_of_users(1000, 1, connections2))

    num_users = 1000
    avg_friendships = 500
    sg = SocialGraph()
    start_time = time.time()
    sg.populate_graph(num_users, avg_friendships)
    end_time = time.time()
    print("\n\n-----")
    print(f"Quadratic populate: {end_time - start_time} seconds")
    print("-----\n\n")
    sg = SocialGraph()
    start_time = time.time()
    sg.populate_graph_linear(num_users, avg_friendships)
    end_time = time.time()
    print(f"Linear populate: {end_time - start_time} seconds")
