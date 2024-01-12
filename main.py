

def main():
    
    book_path = 'books/frankenstein.txt'
    file_contents = get_book_text(book_path)
    count = get_word_count(file_contents)
    char_count = get_char_count(file_contents)
    boot_char_count = boot_get_char_count(file_contents)
    
    get_report(char_count, book_path, count)
    
def get_word_count(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_char_count(text):
    characters = ['a','b','c','d','e','f','g','h','i','j','k','l',
                  'o','p','q','r','s','t','u','v','w','x','y','z']
    lower = text.lower()
    char_count = {}
    for chara in characters:
        char_count[chara] = lower.count(chara)
    return char_count

# given solution for character count
def boot_get_char_count(text):
    count = {}
    for c in text:
        lower = c.lower()
        if lower in count:
            count[lower] += 1
        else:
            count[lower] = 1
    return count

def get_report(data, book_path, word_count):
    list_data = list(data.items())
    sort_data = sorted(list_data, key=lambda x: x[1], reverse=True)

    print(f'--- Begin report of {book_path} ---')
    print(f'{word_count} words found in the document\n')

    for item in sort_data:
        print(f"The '{item[0]}' character was found {item[1]} times")

    print('--- End Report ---')

# given solution to the report function
###
def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
###

main()

