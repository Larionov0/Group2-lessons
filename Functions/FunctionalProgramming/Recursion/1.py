def factorial(num):
    """
    5! = 5 * 4 * 3 * 2 * 1
    3! = 3 * 2 * 1

    f(5) = 5 * f(4)
    f(4) = 4 * f(3) = 4 * 3 * f(2) = 4 * 3 * 2 * f(1) = 4 * 3 * 2 * 1

    f(num) = num * f(num - 1)
    f(1) = 1    - точка зупинки рекурсії
    """
    if num == 1:
        return 1
    return num * factorial(num - 1)


print(factorial(5))
