def get_book_text(file_path):
    with open(file_path) as f:
        full_text = f.read()
        return full_text
    return full_text

def main(file_path):
    wholebook = get_book_text(file_path)
    return wholebook

def count_words(file_path):
    full_text = get_book_text(file_path)
    word_list = full_text.split()
    wordcount = 0
    for word in word_list:
        wordcount += 1
    print(f"{wordcount} words found in the document")
    return



count_words("books/frankenstein.txt")


