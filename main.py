def get_book_text(file_path):
    with open(file_path) as f:
        full_text = f.read()
        return full_text
    return full_text

def main(file_path):
    wholebook = get_book_text(file_path)
    return wholebook

def count_words(full_text):
    wordcount = full_text.split()
    print(f"{wordcount} words found in the document")
    return



main("books/frankenstein.txt")

count_words(wholebook)

