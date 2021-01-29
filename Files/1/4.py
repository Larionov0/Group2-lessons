text_file = open('secret.txt', 'rt')

lines_list = text_file.readlines()
print(lines_list)


text_file.close()
