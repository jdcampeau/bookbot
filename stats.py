def sort_on(items):
    return items[2]

def word_char_analysis(file_path):
    with open(file_path) as f:
        full_text = f.read()
    word_list = full_text.split()
    lowtext = full_text.lower()
    wordcount = 0
    for word in word_list:
        wordcount += 1
    char_dict = {}
    for i in lowtext:
        if i.isalpha():
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1
        else: None
    dict_list = []
    for char in char_dict:
        num=char_dict[char]
        mini_dict=[char,":",num]
        dict_list.append(mini_dict)
    dict_list.sort(reverse=True, key=sort_on)
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {file_path}...")
    print("--------- Word Count ---------")
    print(f"Found {wordcount} total words")
    print("------- Character Count -------")
    for i in dict_list:
        print(f"{i[0]}: {i[2]}")
    print("==========END==========")
    return

