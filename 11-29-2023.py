# def check_unique_titles(book_titles: list[str]):
#     return len(set(book_titles)) == len(book_titles)
#
#
# titles = ['I Was Told There\'d Be Cake', 'Pale Fire', 'Dorothy Must Die', 'Full Dark, No Stars',
#           'Full Dark, No Stars']
#
# print(check_unique_titles(titles))

# x - new and empty file
# w - new file that is writable

file = open('it-3-ya-2.txt', 'r+')

# r - read only
# r+ - read and write
# w - write only
# w+ - write and read
# a - append
# a+ - append and read

print(file.readline())
