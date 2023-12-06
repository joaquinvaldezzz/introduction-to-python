import numpy as np

one = np.array([1, 2, 3, 4, 5])
two = np.array([6, 7, 8, 9, 0])
three = np.concatenate((one, two))
my_range = np.linspace(0, 10, 4)

arith1 = np.array((5, 6, 7, 78))
arith2 = np.array((5, 6, 7, 78))

add = np.add(arith1, arith2)
minus = np.subtract(arith1, arith2)
multi = np.multiply(arith1, arith2)
div = np.divide(arith1, arith2)

print(add)
print(minus)
print(multi)
print(div)

print('Standard Deviation:', np.std(arith1))
print('Mean:', np.mean(arith1))
print('Min:', np.min(arith1))
print('Max:', np.max(arith1))

new = np.reshape(arith1, (2, 2))

print(new)

transfer = np.transpose(np.array([[1, 2, 4], [5, 6, 7]]))
print(transfer)
