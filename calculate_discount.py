# Create a function that will calculate the discounted price of an item
# `int | float` indicates that the parameter should be either an integer or a float
def price_discount(original_price: int | float, discount_percentage: int | float):
    result = original_price - (original_price * discount_percentage // 100)

    print(f'From the original price of {original_price} to discounted price of {result}.')


# Create a function that will ask the user to input the original price and the discount percentage
def input_data():
    # `int | float` indicates that the variable only accepts an integer or a float
    original: int | float = eval(input('Enter original price: '))
    discount: int | float = eval(input('Enter percentage of the discount: '))

    # Return the values so that the `price_discount` function can use it
    return [original, discount]


# Create an instance of the `input_data` function above
output = input_data()

# Call the function that will calculate the discounted price
# [0] being the original price and [1] being the discount percentage
price_discount(output[0], output[1])
