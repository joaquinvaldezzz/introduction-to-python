leap_year = int(input('Enter a year: '))


def check(input_leap: int):
    if (input_leap % 4 == 0 and input_leap % 100 != 0) or (input_leap % 400 == 0):
        return True
    else:
        return False


if check(leap_year):
    print('It is a leap year.')
else:
    print('It is not a leap year.')
