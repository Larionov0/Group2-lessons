def gena(*words):
    for i in range(len(words[0])):
        word_we_need=""
        for word in words:
            word_we_need+=word[i]
        yield word_we_need


for brute_word in gena('lol','kek','wow','bob'):
    print(brute_word)
