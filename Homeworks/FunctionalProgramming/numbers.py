'''
Пользователь вводит числа через пробел. Программа выводит список из тех чисел пользователя,
 которые не делятся на 3. Циклы запрещены.
'''

# odd_numbers = list(filter(lambda number: number % 2 == 0, numbers))

numbers = input('enter numbers:')
numbers_lst = numbers.split(' ')
numbers_lst = list(map(int, numbers_lst))

print(list(filter(lambda number: number % 3 != 0, numbers_lst)))
