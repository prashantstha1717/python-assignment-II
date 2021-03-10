# 11. Create a variable, filename. Assuming that it has a three-letter extension, and using slice operations, find the extension.
# For README.txt, the extension should be txt. Write code using slice operations that will give the name without the extension.
# Does your code work on filenames of arbitrary length?

def get_file_name(filename):
    return filename.split('.')[0]


filename = str(input('Enter a filename with extension: '))
print(get_file_name(f'The file name is {filename}'))
