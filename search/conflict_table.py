# 线性冲突
# 来自网络
conflict_table = dict()

# assumes goal tuple has up to
# for the given pattern it the start position
# how much to add for linear conflicts
# 2 per conflict - max of 6

# goal tuple is ('g0', 'g1', 'g2', 'g3')

conflict_table[('g0', 'g1', 'g2', 'g3')] = 0
conflict_table[('g0', 'g1', 'g2', 'x')] = 0
conflict_table[('g0', 'g1', 'g3', 'g2')] = 2
conflict_table[('g0', 'g1', 'g3', 'x')] = 0
conflict_table[('g0', 'g1', 'x', 'g2')] = 0
conflict_table[('g0', 'g1', 'x', 'g3')] = 0
conflict_table[('g0', 'g1', 'x', 'x')] = 0
conflict_table[('g0', 'g2', 'g1', 'g3')] = 2
conflict_table[('g0', 'g2', 'g1', 'x')] = 2
conflict_table[('g0', 'g2', 'g3', 'g1')] = 4
conflict_table[('g0', 'g2', 'g3', 'x')] = 0
conflict_table[('g0', 'g2', 'x', 'g1')] = 2
conflict_table[('g0', 'g2', 'x', 'g3')] = 0
conflict_table[('g0', 'g2', 'x', 'x')] = 0
conflict_table[('g0', 'g3', 'g1', 'g2')] = 4
conflict_table[('g0', 'g3', 'g1', 'x')] = 2
conflict_table[('g0', 'g3', 'g2', 'g1')] = 4
conflict_table[('g0', 'g3', 'g2', 'x')] = 2
conflict_table[('g0', 'g3', 'x', 'g1')] = 2
conflict_table[('g0', 'g3', 'x', 'g2')] = 2
conflict_table[('g0', 'g3', 'x', 'x')] = 0
conflict_table[('g0', 'x', 'g1', 'g2')] = 0
conflict_table[('g0', 'x', 'g1', 'g3')] = 0
conflict_table[('g0', 'x', 'g1', 'x')] = 0
conflict_table[('g0', 'x', 'g2', 'g1')] = 2
conflict_table[('g0', 'x', 'g2', 'g3')] = 0
conflict_table[('g0', 'x', 'g2', 'x')] = 0
conflict_table[('g0', 'x', 'g3', 'g1')] = 2
conflict_table[('g0', 'x', 'g3', 'g2')] = 2
conflict_table[('g0', 'x', 'g3', 'x')] = 0
conflict_table[('g0', 'x', 'x', 'g1')] = 0
conflict_table[('g0', 'x', 'x', 'g2')] = 0
conflict_table[('g0', 'x', 'x', 'g3')] = 0
conflict_table[('g1', 'g0', 'g2', 'g3')] = 2
conflict_table[('g1', 'g0', 'g2', 'x')] = 2
conflict_table[('g1', 'g0', 'g3', 'g2')] = 4
conflict_table[('g1', 'g0', 'g3', 'x')] = 2
conflict_table[('g1', 'g0', 'x', 'g2')] = 2
conflict_table[('g1', 'g0', 'x', 'g3')] = 2
conflict_table[('g1', 'g0', 'x', 'x')] = 2
conflict_table[('g1', 'g2', 'g0', 'g3')] = 4
conflict_table[('g1', 'g2', 'g0', 'x')] = 4
conflict_table[('g1', 'g2', 'g3', 'g0')] = 6
conflict_table[('g1', 'g2', 'g3', 'x')] = 0
conflict_table[('g1', 'g2', 'x', 'g0')] = 4
conflict_table[('g1', 'g2', 'x', 'g3')] = 0
conflict_table[('g1', 'g2', 'x', 'x')] = 0
conflict_table[('g1', 'g3', 'g0', 'g2')] = 4
conflict_table[('g1', 'g3', 'g0', 'x')] = 4
conflict_table[('g1', 'g3', 'g2', 'g0')] = 6
conflict_table[('g1', 'g3', 'g2', 'x')] = 0
conflict_table[('g1', 'g3', 'x', 'g0')] = 4
conflict_table[('g1', 'g3', 'x', 'g2')] = 2
conflict_table[('g1', 'g3', 'x', 'x')] = 0
conflict_table[('g1', 'x', 'g0', 'g2')] = 2
conflict_table[('g1', 'x', 'g0', 'g3')] = 2
conflict_table[('g1', 'x', 'g0', 'x')] = 2
conflict_table[('g1', 'x', 'g2', 'g0')] = 4
conflict_table[('g1', 'x', 'g2', 'g3')] = 0
conflict_table[('g1', 'x', 'g2', 'x')] = 0
conflict_table[('g1', 'x', 'g3', 'g0')] = 4
conflict_table[('g1', 'x', 'g3', 'g2')] = 2
conflict_table[('g1', 'x', 'g3', 'x')] = 0
conflict_table[('g1', 'x', 'x', 'g0')] = 2
conflict_table[('g1', 'x', 'x', 'g2')] = 0
conflict_table[('g1', 'x', 'x', 'g3')] = 0
conflict_table[('g2', 'g0', 'g1', 'g3')] = 4
conflict_table[('g2', 'g0', 'g1', 'x')] = 4
conflict_table[('g2', 'g0', 'g3', 'g1')] = 4
conflict_table[('g2', 'g0', 'g3', 'x')] = 2
conflict_table[('g2', 'g0', 'x', 'g1')] = 4
conflict_table[('g2', 'g0', 'x', 'g3')] = 2
conflict_table[('g2', 'g0', 'x', 'x')] = 2
conflict_table[('g2', 'g1', 'g0', 'g3')] = 4
conflict_table[('g2', 'g1', 'g0', 'x')] = 4
conflict_table[('g2', 'g1', 'g3', 'g0')] = 6
conflict_table[('g2', 'g1', 'g3', 'x')] = 2
conflict_table[('g2', 'g1', 'x', 'g0')] = 4
conflict_table[('g2', 'g1', 'x', 'g3')] = 2
conflict_table[('g2', 'g1', 'x', 'x')] = 2
conflict_table[('g2', 'g3', 'g0', 'g1')] = 4
conflict_table[('g2', 'g3', 'g0', 'x')] = 4
conflict_table[('g2', 'g3', 'g1', 'g0')] = 6
conflict_table[('g2', 'g3', 'g1', 'x')] = 4
conflict_table[('g2', 'g3', 'x', 'g0')] = 4
conflict_table[('g2', 'g3', 'x', 'g1')] = 4
conflict_table[('g2', 'g3', 'x', 'x')] = 0
conflict_table[('g2', 'x', 'g0', 'g1')] = 4
conflict_table[('g2', 'x', 'g0', 'g3')] = 2
conflict_table[('g2', 'x', 'g0', 'x')] = 2
conflict_table[('g2', 'x', 'g1', 'g0')] = 4
conflict_table[('g2', 'x', 'g1', 'g3')] = 2
conflict_table[('g2', 'x', 'g1', 'x')] = 2
conflict_table[('g2', 'x', 'g3', 'g0')] = 4
conflict_table[('g2', 'x', 'g3', 'g1')] = 4
conflict_table[('g2', 'x', 'g3', 'x')] = 0
conflict_table[('g2', 'x', 'x', 'g0')] = 2
conflict_table[('g2', 'x', 'x', 'g1')] = 2
conflict_table[('g2', 'x', 'x', 'g3')] = 0
conflict_table[('g3', 'g0', 'g1', 'g2')] = 6
conflict_table[('g3', 'g0', 'g1', 'x')] = 4
conflict_table[('g3', 'g0', 'g2', 'g1')] = 6
conflict_table[('g3', 'g0', 'g2', 'x')] = 4
conflict_table[('g3', 'g0', 'x', 'g1')] = 4
conflict_table[('g3', 'g0', 'x', 'g2')] = 4
conflict_table[('g3', 'g0', 'x', 'x')] = 2
conflict_table[('g3', 'g1', 'g0', 'g2')] = 6
conflict_table[('g3', 'g1', 'g0', 'x')] = 4
conflict_table[('g3', 'g1', 'g2', 'g0')] = 6
conflict_table[('g3', 'g1', 'g2', 'x')] = 4
conflict_table[('g3', 'g1', 'x', 'g0')] = 4
conflict_table[('g3', 'g1', 'x', 'g2')] = 4
conflict_table[('g3', 'g1', 'x', 'x')] = 2
conflict_table[('g3', 'g2', 'g0', 'g1')] = 6
conflict_table[('g3', 'g2', 'g0', 'x')] = 4
conflict_table[('g3', 'g2', 'g1', 'g0')] = 6
conflict_table[('g3', 'g2', 'g1', 'x')] = 4
conflict_table[('g3', 'g2', 'x', 'g0')] = 4
conflict_table[('g3', 'g2', 'x', 'g1')] = 4
conflict_table[('g3', 'g2', 'x', 'x')] = 2
conflict_table[('g3', 'x', 'g0', 'g1')] = 4
conflict_table[('g3', 'x', 'g0', 'g2')] = 4
conflict_table[('g3', 'x', 'g0', 'x')] = 2
conflict_table[('g3', 'x', 'g1', 'g0')] = 4
conflict_table[('g3', 'x', 'g1', 'g2')] = 4
conflict_table[('g3', 'x', 'g1', 'x')] = 2
conflict_table[('g3', 'x', 'g2', 'g0')] = 4
conflict_table[('g3', 'x', 'g2', 'g1')] = 4
conflict_table[('g3', 'x', 'g2', 'x')] = 2
conflict_table[('g3', 'x', 'x', 'g0')] = 2
conflict_table[('g3', 'x', 'x', 'g1')] = 2
conflict_table[('g3', 'x', 'x', 'g2')] = 2
conflict_table[('x', 'g0', 'g1', 'g2')] = 0
conflict_table[('x', 'g0', 'g1', 'g3')] = 0
conflict_table[('x', 'g0', 'g1', 'x')] = 0
conflict_table[('x', 'g0', 'g2', 'g1')] = 2
conflict_table[('x', 'g0', 'g2', 'g3')] = 0
conflict_table[('x', 'g0', 'g2', 'x')] = 0
conflict_table[('x', 'g0', 'g3', 'g1')] = 2
conflict_table[('x', 'g0', 'g3', 'g2')] = 2
conflict_table[('x', 'g0', 'g3', 'x')] = 0
conflict_table[('x', 'g0', 'x', 'g1')] = 0
conflict_table[('x', 'g0', 'x', 'g2')] = 0
conflict_table[('x', 'g0', 'x', 'g3')] = 0
conflict_table[('x', 'g1', 'g0', 'g2')] = 2
conflict_table[('x', 'g1', 'g0', 'g3')] = 2
conflict_table[('x', 'g1', 'g0', 'x')] = 2
conflict_table[('x', 'g1', 'g2', 'g0')] = 4
conflict_table[('x', 'g1', 'g2', 'g3')] = 0
conflict_table[('x', 'g1', 'g2', 'x')] = 0
conflict_table[('x', 'g1', 'g3', 'g0')] = 4
conflict_table[('x', 'g1', 'g3', 'g2')] = 2
conflict_table[('x', 'g1', 'g3', 'x')] = 0
conflict_table[('x', 'g1', 'x', 'g0')] = 2
conflict_table[('x', 'g1', 'x', 'g2')] = 0
conflict_table[('x', 'g1', 'x', 'g3')] = 0
conflict_table[('x', 'g2', 'g0', 'g1')] = 4
conflict_table[('x', 'g2', 'g0', 'g3')] = 2
conflict_table[('x', 'g2', 'g0', 'x')] = 2
conflict_table[('x', 'g2', 'g1', 'g0')] = 4
conflict_table[('x', 'g2', 'g1', 'g3')] = 2
conflict_table[('x', 'g2', 'g1', 'x')] = 2
conflict_table[('x', 'g2', 'g3', 'g0')] = 4
conflict_table[('x', 'g2', 'g3', 'g1')] = 4
conflict_table[('x', 'g2', 'g3', 'x')] = 0
conflict_table[('x', 'g2', 'x', 'g0')] = 2
conflict_table[('x', 'g2', 'x', 'g1')] = 2
conflict_table[('x', 'g2', 'x', 'g3')] = 0
conflict_table[('x', 'g3', 'g0', 'g1')] = 4
conflict_table[('x', 'g3', 'g0', 'g2')] = 4
conflict_table[('x', 'g3', 'g0', 'x')] = 2
conflict_table[('x', 'g3', 'g1', 'g0')] = 4
conflict_table[('x', 'g3', 'g1', 'g2')] = 4
conflict_table[('x', 'g3', 'g1', 'x')] = 2
conflict_table[('x', 'g3', 'g2', 'g0')] = 4
conflict_table[('x', 'g3', 'g2', 'g1')] = 4
conflict_table[('x', 'g3', 'g2', 'x')] = 2
conflict_table[('x', 'g3', 'x', 'g0')] = 2
conflict_table[('x', 'g3', 'x', 'g1')] = 2
conflict_table[('x', 'g3', 'x', 'g2')] = 2
conflict_table[('x', 'x', 'g0', 'g1')] = 0
conflict_table[('x', 'x', 'g0', 'g2')] = 0
conflict_table[('x', 'x', 'g0', 'g3')] = 0
conflict_table[('x', 'x', 'g1', 'g0')] = 2
conflict_table[('x', 'x', 'g1', 'g2')] = 0
conflict_table[('x', 'x', 'g1', 'g3')] = 0
conflict_table[('x', 'x', 'g2', 'g0')] = 2
conflict_table[('x', 'x', 'g2', 'g1')] = 2
conflict_table[('x', 'x', 'g2', 'g3')] = 0
conflict_table[('x', 'x', 'g3', 'g0')] = 2
conflict_table[('x', 'x', 'g3', 'g1')] = 2
conflict_table[('x', 'x', 'g3', 'g2')] = 2


def linear_conflicts(start_list, goal_list):
    """
    calculates number of moves to add to the estimate of
    the moves to get from start to goal based on the number
    of conflicts on a given row or column. start_list
    represents the current location and goal_list represnts
    the final goal.
    """

    # Find which of the tiles in start_list have their goals on this line
    # build a pattern to use in a lookup table of this form:
    # g0, g1, g3, g3 fill in x where there is no goal for this line

    # all 'x' until we file a tile whose goal is in this line

    goal_pattern = ['x', 'x', 'x', 'x']

    for g in range(4):
        for s in range(4):
            start_tile_num = start_list[s]
            if start_tile_num == goal_list[g] and start_tile_num != 0:
                goal_pattern[s] = 'g' + str(g)  # i.e. g0

    global conflict_table

    tup_goal_pattern = tuple(goal_pattern)

    if tup_goal_pattern in conflict_table:
        return conflict_table[tuple(goal_pattern)]
    else:
        return 0


def listconflicts(goal_list):
    """
    list all possible start lists that will have at least
    one linear conflict.

    Possible goal tile configurations

    g g g g
    g g g x
    g g x g
    g x g g
    x g g g
    g g x x
    g x g x
    g x x g
    x g g x
    x g x g
    x x g g

    """

    all_tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    non_goal_tiles = []

    for t in all_tiles:
        if t not in goal_list:
            non_goal_tiles.append(t)

    combinations = dict()

    # g g g g

    for i in goal_list:
        tile_list2 = goal_list[:]
        tile_list2.remove(i)
        for j in tile_list2:
            tile_list3 = tile_list2[:]
            tile_list3.remove(j)
            for k in tile_list3:
                tile_list4 = tile_list3[:]
                tile_list4.remove(k)
                for l in tile_list4:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list, goal_list)
                    if conflictadd > 0:
                        combinations[start_list] = conflictadd

                        # g g g x

    for i in goal_list:
        tile_list2 = goal_list[:]
        tile_list2.remove(i)
        for j in tile_list2:
            tile_list3 = tile_list2[:]
            tile_list3.remove(j)
            for k in tile_list3:
                for l in non_goal_tiles:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list, goal_list)
                    if conflictadd > 0:
                        combinations[start_list] = conflictadd

                        # g g x g

    for i in goal_list:
        tile_list2 = goal_list[:]
        tile_list2.remove(i)
        for j in tile_list2:
            tile_list3 = tile_list2[:]
            tile_list3.remove(j)
            for k in non_goal_tiles:
                for l in tile_list3:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list, goal_list)
                    if conflictadd > 0:
                        combinations[start_list] = conflictadd
    # g x g g

    for i in goal_list:
        tile_list2 = goal_list[:]
        tile_list2.remove(i)
        for j in non_goal_tiles:
            for k in tile_list2:
                tile_list3 = tile_list2[:]
                tile_list3.remove(k)
                for l in tile_list3:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list, goal_list)
                    if conflictadd > 0:
                        combinations[start_list] = conflictadd

    # x g g g

    for i in non_goal_tiles:
        for j in goal_list:
            tile_list2 = goal_list[:]
            tile_list2.remove(j)
            for k in tile_list2:
                tile_list3 = tile_list2[:]
                tile_list3.remove(k)
                for l in tile_list3:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list, goal_list)
                    if conflictadd > 0:
                        combinations[start_list] = conflictadd

    # g g x x

    for i in goal_list:
        tile_list2 = goal_list[:]
        tile_list2.remove(i)
        for j in tile_list2:
            tile_list3 = tile_list2[:]
            tile_list3.remove(j)
            for k in non_goal_tiles:
                tile_list4 = non_goal_tiles[:]
                tile_list4.remove(k)
                for l in tile_list4:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list, goal_list)
                    if conflictadd > 0:
                        combinations[start_list] = conflictadd

                        # g x g x

    for i in goal_list:
        tile_list2 = goal_list[:]
        tile_list2.remove(i)
        for j in non_goal_tiles:
            tile_list3 = non_goal_tiles[:]
            tile_list3.remove(j)
            for k in tile_list2:
                for l in tile_list3:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list, goal_list)
                    if conflictadd > 0:
                        combinations[start_list] = conflictadd

                        # g x x g

    for i in goal_list:
        tile_list2 = goal_list[:]
        tile_list2.remove(i)
        for j in non_goal_tiles:
            tile_list3 = non_goal_tiles[:]
            tile_list3.remove(j)
            for k in tile_list2:
                for l in tile_list3:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list, goal_list)
                    if conflictadd > 0:
                        combinations[start_list] = conflictadd

                        # x g g x

    for i in non_goal_tiles:
        tile_list2 = non_goal_tiles[:]
        tile_list2.remove(i)
        for j in goal_list:
            tile_list3 = goal_list[:]
            tile_list3.remove(j)
            for k in tile_list3:
                for l in tile_list2:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list, goal_list)
                    if conflictadd > 0:
                        combinations[start_list] = conflictadd

                        # x g x g

    for i in non_goal_tiles:
        tile_list2 = non_goal_tiles[:]
        tile_list2.remove(i)
        for j in goal_list:
            tile_list3 = goal_list[:]
            tile_list3.remove(j)
            for k in tile_list3:
                for l in tile_list2:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list, goal_list)
                    if conflictadd > 0:
                        combinations[start_list] = conflictadd

                        # x x g g

    for i in non_goal_tiles:
        tile_list2 = non_goal_tiles[:]
        tile_list2.remove(i)
        for j in tile_list2:
            for k in goal_list:
                tile_list3 = goal_list[:]
                tile_list3.remove(k)
                for l in tile_list3:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list, goal_list)
                    if conflictadd > 0:
                        combinations[start_list] = conflictadd

    return combinations

