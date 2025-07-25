def count_characters(text):
    characters = {}
    lowercase = text.lower() #to avoid duplicates
    for character in lowercase:
        if character not in characters:
            characters[character] =  1
        else:
            characters[character] +=  1
    return characters


def count_words(text):
    splited_text = text.split()
    return len(splited_text)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def sort_list(characters):
    character_list = []
    for character in characters:
        if character.isalpha():
            ch_num_dic = {"character": character, "num": characters[character]}
            character_list.append(ch_num_dic)
    character_list.sort(reverse=True, key=sort_on)
    return character_list


def sort_on(items):
    return items["num"]