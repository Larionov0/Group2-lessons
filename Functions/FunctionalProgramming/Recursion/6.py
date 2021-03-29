def _list_sum(lst, ready_sum):
    """
    f([1, 2, 3]) = f([1, 2, 3], 0) = f([1, 2], 3) = f([1], 5) = f([], 6) = 6
    """
    if len(lst) == 0:
        return ready_sum
    return _list_sum(lst[:-1], ready_sum + lst[-1])


def list_sum(lst):
    return _list_sum(lst, 0)


print(list_sum([1, 6, 3, 4]))
