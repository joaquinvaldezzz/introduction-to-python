"""
Author:         John Joaquin A. Valdez
Date created:   December 6, 2023,
Description:    A simple program that adds products to a text file and reads its contents.
"""

file_name = 'product_inventory.txt'
open(file_name, 'w')  # Create a text file


# This function adds a product to the text file, and only accepts the following parameters:
# string name, integer quantity, float price, and string txt_file
def add_product(name: str, quantity: int, price: float, txt_file: str):
    try:
        # Open the file in append mode
        with open(txt_file, 'a') as inventory:
            inventory.write(f'{name}, {quantity}, {price}\n')

        print(f'\nProduct {name} added successfully.\n')
        inventory.close()  # Close the file to save memory
    except Exception as error:
        print(f'Error: {error}')


# This function reads the products from the text file, and only accepts the following parameter:
# string txt_file
def read_products(txt_file: str):
    try:
        print(f'\nReading lines from {txt_file}.\n')

        # Open the file in read mode
        with open(txt_file, 'r') as inventory:
            for x in inventory:
                (name, quantity, price) = x.strip().split(', ')
                print(f'Name: {name}, Quantity: {quantity}, Price: {price}')

        print()  # Print a new line
        inventory.close()  # Close the file to save memory
    except FileNotFoundError:
        print(f'File {txt_file} not found.')
    except Exception as error:
        print(f'Error: {error}')


# This is the main function of the program
def main():
    while True:
        print('1. Add a product')
        print('2. View Product Inventory')
        print('3. Exit\n')

        user_choice = int(input('Enter your choice: '))

        # This condition checks if the user choice is equal to 1
        if user_choice == 1:
            # This block of code asks the user to input the product details
            product_name = input('\nEnter product name: ')
            product_quantity = int(input('Enter product quantity: '))
            product_price = float(input('Enter product price: '))

            # This function call adds the product to the text file
            add_product(product_name, product_quantity, product_price, file_name)
        elif user_choice == 2:
            # This function call reads the products from the text file
            read_products(file_name)
        elif user_choice == 3:
            # This block of code terminates the program
            print('\nProgram terminated.')
            break
        else:
            # This block of code prints an error message if the user choice is not equal to 1, 2,
            # or 3
            print('Invalid choice.')


if __name__ == '__main__':
    main()
