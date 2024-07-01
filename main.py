def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    num_words = get_num_words(text)
    num_char_list = sort_data(get_num_chars(text))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print_char_list(num_char_list)
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_path(path):
    with open(path) as f:
        return f.read()
    
def get_num_chars(text):
    num_char_dict = {}

    for char in text:
        lowered = char.lower()
        if lowered in num_char_dict:
            num_char_dict[lowered] += 1
        else:
           num_char_dict[lowered] = 1 

    return num_char_dict

def sort_on(dict):
    return dict["num"]

def sort_data(char_dict):

    char_list = []
    for item in char_dict:
        if item.isalpha():
            char_list.append({"name": item, "num": char_dict[item]})
    char_list.sort(reverse=True, key=sort_on)

    return char_list

def print_char_list(char_list):

    for item in char_list:
        print(f"The {item['name']} character was found {item['num']} times")

main()
