def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_number_of_words(text)
    chars_dictionary = count_characters(text)
    chars_sorted_list = chars_dictionary_to_sorted_list(chars_dictionary)

    print(f"--- Book report of {book_path} ---")
    print(f"{num_words} words found")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"Character '{item['char']}' was found {item['num']} times")

    print ("--- End of Report ---")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_number_of_words(booktext):
    words = booktext.split()
    return len(words)

def count_characters(booktext):
    char_count = {}
    for chars in booktext:
        lowered = chars.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1
    return char_count

def sort_on(d):
    return d["num"]

def chars_dictionary_to_sorted_list(chars_dictionary):
    sorted_list = []
    for ch in chars_dictionary:
        sorted_list.append({"char": ch, "num": chars_dictionary[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()

