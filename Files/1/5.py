text_file = open('secret.txt', 'rt')

for line in text_file:
    print(line)

text_file.close()
