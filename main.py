def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    print(text)

    wordCount = word_count(text)
    print(f"{wordCount} words in this book")

    charCount = char_count(text)
    print(charCount)




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

main()