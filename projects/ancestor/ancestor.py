
def create_family_tree_inverse(family):
    family_tree = {}
    # for each relationship in family
    # add the person and their relation to other family members
    for [parent, child] in family:
        # check if
        if child not in family_tree:
            family_tree[child] = set()
        family_tree[child].add(parent)
        if parent not in family_tree:
            family_tree[parent] = set()

    return family_tree


def find_earliest(ancestors, start, current=None):
    # does start node have parents?
    parents = ancestors[start]
    # if it does
    if len(parents):
        # get parent with smallest value
        smallest_parent = min(parents)
        # call recursively
        return find_earliest(ancestors, smallest_parent, smallest_parent)
    # no parents
    else:
        # are we at the start?
        if current is None:
            return -1
        # if not return the value of the current node
        return current


def earliest_ancestor(ancestors, starting_node):
    reverse_family = create_family_tree_inverse(ancestors)

    return find_earliest(reverse_family, starting_node)


if __name__ == '__main__':
    test_family = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    # print(create_family_tree(test_family))
    # print(create_family_tree_inverse(test_family))

    print(earliest_ancestor(test_family, 1))
