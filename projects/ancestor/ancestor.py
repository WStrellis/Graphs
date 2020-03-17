from collections import deque


def create_family_tree(family):
    family_tree = {}
    # for each relationship in family
    # add the person and their relation to other family members
    for [parent, child] in family:
        # check if
        if parent not in family_tree:
            family_tree[parent] = {'parents': [], 'children': [child]}
        else:
            family_tree[parent]['children'].append(child)
        if child not in family_tree:
            family_tree[child] = {'parents': [parent], 'children': []}
        else:
            family_tree[child]['parents'].append(parent)

    return family_tree


# class Family:
#     def __init__(self):
#         self.members = {}

#     def  create_family_tree(self,family):
#         family_tree = {}
#         # for each relationship in family
#         # each family member must be represented
#         for person in family:
#             # check if
#             if

# class FamilyMember:
#     def __init__(self, id,parents, children):
#         self.id = id
#         self.parents = parents
#         self.children = children

def earliest_ancestor(ancestors, starting_node, oldest_ancestor=-1):

    # create Adjacency list from ancestors
    # store the parent and child for each node
    """
    {1: {
        parents: [10],
        children: [3]
    },
    3: {
        parents: [1,2],
        children:[6]
    }
    }
    """
    # BFS
    # look for parents
    #  set oldest_ancestor to the smallest parent node
    # if no parents and oldest_ancestor is None return -1
    # else if no parents return oldest_ancestor
    # go to all  of the parents for the start_node
    # add all parents to stack
    # if any of the ancestors have a parent go to the parent
    # if not, set oldest_ancestor to the smallest parent node and return
    pass


if __name__ == '__main__':
    test_family = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(create_family_tree(test_family))
