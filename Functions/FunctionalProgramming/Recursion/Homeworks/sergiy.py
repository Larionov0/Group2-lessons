def sum_of_digits(number):
    if number == 0:
        return 0

    last_digit = number % 10
    new_number = number // 10

    return last_digit + sum_of_digits(new_number)


print(sum_of_digits(11255))
