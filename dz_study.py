max = 1
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


def find_farthest_orbit(orbits):
    max = 1
    for i in orbits:
        if i[0] != i[1] and i[0] * i[1] > max:
            max = i[0] * i[1]
            index = i
    return index


print(*find_farthest_orbit(orbits))

# def find_farthest_orbit(orbits):
#     max = 1
#     index = 0
#     for i in range(len(orbits)):
#         lst = list(orbits[i])
#         if lst[0] * lst[1] > max and lst[0] != lst[1]:
#             max = lst[0] * lst[1]
#             index = i
#     return orbits[index]
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
