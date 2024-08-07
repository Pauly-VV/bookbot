def main():
    path = "books/frankenstein.txt"
    text = get_text(path)

    wordCount = word_count(text)

    charCount = char_count(text)

    sorted = char_sort(charCount)
    
    print(sorted)
    print(sorted[0])
    print(sorted[0]["char"])
    print(sorted[0]["num"])

    report(sorted, wordCount, path)

def word_count(text):
    word_list = text.split()
    return len(word_list)

def get_text(path):
    with open(path) as f:
        return f.read()

def char_count(text):
    letter_dict = {}
    text_lower = text.lower()
    for letter in text_lower:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def report(char_dict_list, word_count, path):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")

    for c in range(len(char_dict_list)):
        print(f"The {char_dict_list[c]['char']} character was found {char_dict_list[c]['num']} times")

    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def char_sort(char_dict):
    char_dict_list = []
    for char in char_dict:
        if char.isalpha():
            new_dict = {"char":char, "num":char_dict[char]}
            char_dict_list.append(new_dict)
            

    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list

main()