def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    # Count characters
    chars_dict = {}
    for char in text:
        char = char.lower()
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    
    # Convert to list of dictionaries
    chars_list = []
    for char, count in chars_dict.items():
        chars_list.append({"char": char, "num": count})
    
    # Sort the list
    def sort_on(dict):
        return dict["num"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list