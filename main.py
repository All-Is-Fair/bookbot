import sys
from stats import get_book_text, get_num_words, get_characters

import sys

# Check if we have enough arguments
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# If we get here, we can use sys.argv[1] as the book path
book_path = sys.argv[1]
# Continue with your existing code, using book_path instead of hardcoded "books/frankenstein.txt"

def print_report(path, word_count, chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print only alphabetical characters
    for char_dict in chars_list:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict['num']}")
    
    print("============= END ===============")

# Main code

text = get_book_text(book_path)
word_count = get_num_words(text)
chars_list = get_characters(text)

# Call the print_report function
print_report(book_path, word_count, chars_list)