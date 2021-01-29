text_file = open('secret.txt', 'rt')

text = text_file.readline()
print(text)
text = text_file.readline()
print(text)

text_file.close()
