def helloer(name):
    print(f'Hello, {name}')


def nastinnyy_nadpys(name1, name2):
    print(f'{name1} + {name2} = любов')


def summer(a, b):
    result = a + b
    return result


def calculator(n1, n2, sign):
    if sign == '+':
        return n1 + n2
    elif sign == '-':
        return n1 - n2
    elif sign == '*':
        return n1 * n2
    elif sign == '/':
        return n1 / n2
    elif sign == '^':
        result = 1
        i = 0
        while i < n2:
            result *= n1
            i += 1

        return result

    elif sign == '#':
        return (n1 - n2) * (n1 + n2)


def list_sum(lst):
    sum_ = 0
    for number in lst:
        sum_ += number
    return sum_


def print_line(n=40):
    print('-' * n)


def my_range(n1, n2=None, step=1):
    if n2 is None:
        start = 0
        stop = n1
    else:
        start = n1
        stop = n2

    numbers = []
    n = start
    while n < stop:
        numbers.append(n)
        n += step
    return numbers


def input_int(text, error_message='Це не число! Спробуйте ще раз.', min_value=None, max_value=None):
    while True:
        number_str = input(text)  # '213d'
        if number_str.isdigit():
            number = int(number_str)
            if min_value is not None:
                if number < min_value:
                    print('Замале число!')
                    continue

            if max_value is not None:
                if number > max_value:
                    print('Завелике число!')
                    continue

            return number
        else:
            print(error_message)


def many_people_welcome(*names, msg='Welcome!'):
    print(msg)
    for name in names:
        print(f"Hello, {name}")


def lol(a, b, value):
    sum = a + b
    print(value)
    return sum


def create_matrix(n, m, value='-'):
    matrix = []
    for _ in range(n):
        row = [value for _ in range(m)]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:  # row=[4, '1', 6, 2, 5]
        row_text = '|'
        for el in row:
            row_text += str(el) + ' '
        row_text = row_text[:-1] + '|'
        print(row_text)


matrix1 = create_matrix(2, 3)
print_matrix(matrix1)

matrix2 = create_matrix(30, 20)
print_matrix(matrix2)
