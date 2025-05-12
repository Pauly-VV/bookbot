from stats import *
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    path = str(sys.argv[1])
    text = get_text(path)

    wordCount = word_count(text)

    charCount = char_count(text)

    sorted = char_sort(charCount)

    report(sorted, wordCount, path)

def get_text(path):
    with open(path) as f:
        return f.read()

def report(char_dict_list, word_count, path):
    print("============ BOOKBOT ============")
    print(f"----- Begin report of {path} -----")
    print("---------- Word Count -----------")
    print(f"{word_count} words found in the document\n")
    print("-------- Character Count --------")
    for c in range(len(char_dict_list)):
        print(f"{char_dict_list[c]['char']}: {char_dict_list[c]['num']}")

    print("--- End report ---")

main()