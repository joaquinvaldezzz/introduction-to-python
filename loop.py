rows = 5

for x in range(1, rows + 1):
    print(' ' * (rows - x) + '*' * (2 * x - 1))

for y in range(rows - 1, -1, -1):
    print(' ' * (rows - y) + '*' * (2 * y - 1))
