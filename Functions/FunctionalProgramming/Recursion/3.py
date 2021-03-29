def list_sum(numbers):
    """
    Повертає суму чисел списка

    f([1, 6, 3, 4]) = 4 + f([1, 6, 3]) = 4 + 3 + f([1, 6]) =
    = 4 + 3 + 6 + f([1]) = 4 + 3 + 6 + 1 + f([]) = 4 + 3 + 6 + 1 + 0
    """
    if len(numbers) == 0:
        return 0

    last_num = numbers.pop(-1)
    return last_num + list_sum(numbers)


print(list_sum([1, 6, 3, 4]))
