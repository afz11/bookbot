def main ():
    book_path = "books/frankestein.txt"
    text = get_book_text(book_path)
    words_count = word_count(text)
    count_dict = char_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(count_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(book):
    return len(book.split())

def char_count(string):
    chars = {}

    for char in string:
        lowered = char.lower()
        if lowered not in chars:
            chars[lowered] = 1
        else:
            chars[lowered]  += 1
    
    return chars

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})  
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
main()