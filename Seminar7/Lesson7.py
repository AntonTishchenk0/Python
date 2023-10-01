# Task 26
# def power(a, b):
#     if b == 0:
#         return 1
#     return power(a, b - 1) * a
#
#
# print(power(5, 3))
# power(5, 3) -> power(5, 2) * 5 = 1 * 5 * 5 * 5 = 125
#                |
#                power(5, 1) * 5 = 1 * 5 * 5
#                |
#                power(5, 0) * 5 = 1 * 5
#                |
#                1


# Task 47

# trasformation = lambda x: x
#
# values = [1, 23, 42, 'asdf']
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# s = input().split()
# print(s)
# data = lambda x: int(x)
# a = list(map(data, s))
# print(a)
# filter <-> map
# data = lambda x: int(x)


# Task 49
# def find_farthest_orbit(orbits):
#     condition = lambda data: (data[0] != data[1]) * data[0] * data[1]
#     square_orbits = list(map(condition, orbits))
#     return orbits[square_orbits.index(max(square_orbits))]
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Task 51
# def same_by(characteristic, objects):
#     # print(set(map(characteristic, objects)))
#     return len(set(map(characteristic, objects))) in (0, 1)


# values = [7, 11, 15, 19]
# if same_by(lambda x: x % 4, values):
#     print('same')
# else:
#     print('different')