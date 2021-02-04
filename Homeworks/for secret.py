parol = input("введіть пароль: ")
file = open("secret.txt")
text = file.read()
paswd = open('password.txt')
real_psswd = paswd.read()
if parol == real_psswd:
    print(text)
else:
    print('невірний пароль')
