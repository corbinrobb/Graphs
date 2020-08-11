
def earliest_ancestor(ancestors, starting_node):
    d = {}

    for node in ancestors:
        if node[1] not in d:
            d[node[1]] = [node[0]]
        else:
            d[node[1]].append(node[0])

    cur = starting_node

    if cur not in d:
        return -1

    while cur in d:
        cur = d[cur][0]

    return cur
