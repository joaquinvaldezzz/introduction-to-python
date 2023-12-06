txt_file = 'it-3-ya-2.txt'
user_text = input('Enter text: ')


def enter_text(file: str, user_input: str | int):
    try:
        # Open the file in write mode
        with open(file, 'w') as f:
            f.write(user_input)

        print(f'Text entered successfully in the {file}.')
        f.close()  # Close the file to save memory
    except Exception as error:
        print(f'Error: {error}')


def read_text(file: str):
    try:
        print(f'\nReading lines from the {file}.')

        # Open the file in read mode
        with open(file, 'r') as f:
            print(f.read())

        f.close()  # Close the file to save memory
    except FileNotFoundError:
        print(f'File {file} not found.')
    except Exception as error:
        print(f'Error: {error}')


enter_text(txt_file, user_text)
read_text(txt_file)
