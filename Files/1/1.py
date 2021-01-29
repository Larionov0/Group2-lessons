file = open('secret.txt', 'rt')

text = file.read()
print(text)

file.close()
