# num = [[c for c in range(r)] for r in range(6)]
# for x in num:
#     if len(x) < 4:
#         print(x)

# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# list1.extend(list2)
# list1.reverse()
# print(list1)

# list1 = ['a', 'b', 'c']
# list2 = list(('apple', 'banana',))
# list2.insert(3, 'cherry')
# list2.reverse()
# list1.extend(list2)
# print(list1)

fruits = ('apple', 'banana', 'cherry', 'strawberry', 'raspberry')
(*first, second, third) = fruits

print(first)  # Prints apple
print(second)  # Prints ['banana', 'cherry']
print(third)  # Prints strawberry
# print(fourth)  # Prints raspberry

# print(second)
# print(third)
# print(fourth)
# print(fifth)
