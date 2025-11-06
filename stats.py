

def get_num_words(book_content):
    num_words = len(book_content.split())
    print(f"Found {num_words} total words")

def print_sorted_char_dict(book_content):
    words_list = book_content.split()
    char_dict = {}

    for word in words_list:
        chars_list = list(word)
        for char in chars_list:
            if (char.isalpha() is True):
                if (char.lower() not in char_dict):
                    char_dict[char.lower()] = 1
                else:
                    char_dict[char.lower()] += 1

    # print(char_dict)
    return dict_sorter(char_dict)

def dict_sorter(char_dict):
    dict_keys = list(char_dict.keys())
    formatted_dict_list = []
    for key in dict_keys:
        dict_item = {
            "char": key,
            "num": char_dict[key]
        }
        formatted_dict_list.append(dict_item)
    return formatted_dict_list

