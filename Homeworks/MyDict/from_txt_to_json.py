import json
def load_words():
    '''
    return: words  (dict)
    '''

    with open('words.txt', 'rt', encoding='UTF-8') as file:
        dct = {}
        for line in file:
            lst = line.rstrip().split(' – ')
            dct[lst[0]] = lst[1]
        return dct

words = load_words()

def write_file(words):
    with  open('words.json', 'w', encoding='utf-8') as file:
        json.dump(words, file, ensure_ascii=False)

def to_load_data():
    with open('words.json', 'r') as file:
        data = json.load(file)
        return data

write_file(words)

print(to_load_data())
