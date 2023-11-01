#A. No. Lines, words, char
def count_file_stats(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        num_lines = len(content.split('\n'))
        num_words = len(content.split())
        num_chars = len(content)

        return num_lines, num_words, num_chars

file_path = 'sample.txt'  # Replace with the path to your file
lines, words, characters = count_file_stats(file_path)

print(f'Number of lines: {lines}')
print(f'Number of words: {words}')
print(f'Number of characters: {characters}')


#b. Python program to display files available in the current directory:

import os

def list_files_in_current_directory():
    files = os.listdir('.')
    return [f for f in files if os.path.isfile(f)]

files_in_current_dir = list_files_in_current_directory()

print("Files in current directory:")
for file in files_in_current_dir:
    print(file)
