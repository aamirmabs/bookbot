import sys
from stats import get_num_words, print_sorted_char_dict

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
        
    # print(contents)
    # get_num_words(contents)
    # get_num_chars(contents)
    return contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_content = get_book_text(sys.argv[1])
        # print report
        print('''============ BOOKBOT ============
 Analyzing book found at books/frankenstein.txt...
 ----------- Word Count ----------''')
        get_num_words(book_content)
        print("--------- Character Count -------")
        sorted_dict = print_sorted_char_dict(book_content)
        for item in sorted_dict:
            print(f'{item["char"]}: {item["num"]}')
        print("============= END ===============")
        



main()
