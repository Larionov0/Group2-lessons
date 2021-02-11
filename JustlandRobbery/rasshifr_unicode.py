file = open('Странное письмо.txt', 'rt')

text = ''
lst = file.read().rstrip().split(' ')
for el in lst:
    text += chr(int(el))

file.close()

file = open('Расшифр. Странное письмо.txt', 'wt', encoding='utf-8')
file.write(text)
file.close()
