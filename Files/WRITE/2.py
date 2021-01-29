for _ in range(10):
    file = open('Files/test2.txt', 'at')  # додаємо в кінець файлу

    file.write('I love Python\n')
    file.write('I am sausage\n')

    file.close()
