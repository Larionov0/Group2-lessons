import time


def printer_decor(printer_func):
    def new_printer(*args, **kwargs):
        print('-' * 40)
        printer_func(*args, **kwargs)
        print('-' * 40)
    return new_printer


def time_decor(func):
    def new_func(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(t2 - t1)
        return res
    return new_func


@printer_decor
def helloer(name):
    print(f'Hello, {name}')


@time_decor
def print_list(lst):
    for el in lst:
        print('-', el)
    return 10


@printer_decor
def hero_say(name, text):
    print(f"{name}: {text}")


a = print_list(list(range(100000)))

print(a)
