def input_list():
    # Accepts a list of integers (only) from the user
    elements = list(map(int, input('Enter elements separated by comma: ').split(',')))

    if not elements:
        print('Empty list.')
        exit()
    else:
        return elements


def calculate_list(action: int, user_list: list[int]):
    if not user_list:
        return 'Empty list'

    # If the action is 1, return the list with each element raised to the power of 2
    if action == 1:
        return [i ** 2 for i in user_list]
    # If the action is 2, return the list with each element raised to the power of 3
    elif action == 2:
        return [i ** 3 for i in user_list]
    # If the action is neither 1 nor 2, return an error-like message
    else:
        return 'Invalid action.'


# Prints the actions available to the user
print('Enter your choice of action:')

for index in [1, 2]:
    print(f'- Action #{index}: Raise each element by {index}')

# Asks the user to enter their choice of action
user_action = int(input('\nEnter your choice: '))

# If the user's choice of action is neither 1 nor 2, exit the program
if user_action not in (1, 2):
    print('Invalid action.')
    exit()

# Asks the user to enter a list of elements
user_elements = input_list()

# Calculates the result based on the user's choice of action and list of elements
result = calculate_list(user_action, user_elements)

# Prints the result
print('\nResult:', result)
