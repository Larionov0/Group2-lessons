def printer(a, b):
    """
    Має вивести всі числа від a до b

    printer(1, 5) -> *print(1) ->
    printer(2, 5) -> *print(2) ->
    printer(3, 5) -> *print(3) ->
    printer(4, 5) -> *print(4) ->
    printer(5, 5) -> *print(5)  !stop
    """
    print(a)

    if a == b:  # точка зупинки
        return

    printer(a + 1, b)


printer(5, 10)
