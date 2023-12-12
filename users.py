"""
Author:         John Joaquin A. Valdez
Date created:   December 6, 2023,
Description:    A simple program that adds users to a set and reads its contents.
"""


def add_user(user_details, user_id, username, user_password):
    system_user = {'user_id': user_id, 'user_password': user_password, 'username': username}
    user_details[user_id] = system_user

    print(f'\nUser {user_id} added successfully.\n')


def view_users(user_details):
    if user_details:
        print()

        for user_id, system_user in user_details.items():
            print(
                f"User ID: {user_id}, "
                f"Username: {system_user['username']}, "
                f"Password: {system_user['user_password']}")

        print()
    else:
        print('\nNo contacts or users available here.\n')


def main():
    user_list = {}

    while True:
        print('1. Add a user')
        print('2. View users')
        print('3. Exit\n')

        user_choice = int(input('Enter your choice: '))

        if user_choice == 1:
            user_id = input('\nEnter user ID: ')
            username = input('Enter username: ')
            user_password = input('Enter user password: ')

            add_user(user_list, user_id, username, user_password)
        elif user_choice == 2:
            view_users(user_list)
        elif user_choice == 3:
            break
        else:
            print('Invalid choice.')


if __name__ == '__main__':
    main()
