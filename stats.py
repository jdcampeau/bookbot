def count_words(file_path):
    with open(file_path) as f:
        full_text = f.read()
    word_list = full_text.split()
    wordcount = 0
    for word in word_list:
        wordcount +=1
    print(f"{wordcount} words found in the document")
    return

def character_count(file_path):
    with open(file_path) as f:
        full_text = f.read()
    lowtext = full_text.lower()
    char_dict = {}
    for i in lowtext:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    print(char_dict)
    return


