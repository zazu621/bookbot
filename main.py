
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = numberOfWords(text)
    chars_dict =count_number_characters(text)
    report = create_list(chars_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()

    for item in report:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_book_text(path):
    with open (path) as f:
        return f.read()

def numberOfWords(book_content):
    words =book_content.split()
    count = 0
    for w in words:
        count += 1
    return(count)

def count_number_characters(text):
    my_dictionary = {}
    for c in text:
        lowered_string = c.lower()
        if lowered_string in my_dictionary:
            my_dictionary [lowered_string] +=1
        else:
            my_dictionary [lowered_string] = 1   
    return my_dictionary


def sort_on(dict):
    return dict["num"]

def create_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch,"num": chars_dict[ch]})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list




main()
