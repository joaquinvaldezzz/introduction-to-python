# Hello! My name is {bot_name}.
# I was created in {birth_year}.

name: str = 'Joaquin'

try:
    chatbot_name: str = input('What would be the name of your chat bot?: ').capitalize()
    chatbot_year: int = int(input('When it was created?: '))

    print(f'\n\tHello! My name is {chatbot_name}.')
    print(f'\tI was created in {chatbot_year}.')
except ValueError:
    print(ValueError.__doc__)
