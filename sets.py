set_1 = frozenset({1, 3, 4, 5, 6})
set_2 = frozenset({7, 8, 9, 10, 11, 12, 2, 5, 6})
result = set_1.symmetric_difference(set_2)

# set_1 += set_2  # Union |
# set_1 &= set_2  # Intersection &
# set_1 -= set_2  # Difference -
# set_1 ^= set_2  # Symmetric difference ^

print(set_1)
