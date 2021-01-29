# читання по символам

file = open('secret.txt', 'rt')

text = file.read(4)
print(text)
text = file.read(6)
print(text)
text = file.read()
print(text)
print('---------')
text = file.read()
print(text)

file.close()
