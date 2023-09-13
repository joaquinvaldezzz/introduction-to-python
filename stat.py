import random
from statistics import mean

my_list: list[int] = []

# Create a list of `int` using the `random` module and for-loop
for i in range(0, 6):
    # Generate a random number between 1 and 10
    number = random.randint(1, 10)

    # Append the number to the list
    my_list.append(number)

# Calculate the mean of the list using the `statistics` module
result = mean(my_list)

# Print the list and the mean
print(f"List: {my_list}")
print(f"Mean: {result}")
