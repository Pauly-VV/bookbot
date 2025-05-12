def word_count(text):
    word_list = text.split()
    return len(word_list)

def char_count(text):
    letter_dict = {}
    text_lower = text.lower()
    for letter in text_lower:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def char_sort(char_dict):
    char_dict_list = []
    for char in char_dict:
        if char.isalpha():
            new_dict = {"char":char, "num":char_dict[char]}
            char_dict_list.append(new_dict)
            
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list

def sort_on(dict):
    return dict["num"]