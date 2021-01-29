while True:
    try:
        age = input('Age: ')
        break
    except ValueError:
        print('Помилка. Спробуй ще')

print(age + 1)
