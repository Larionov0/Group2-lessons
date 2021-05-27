from colorama import Fore, init


init()


colors = {
    'червоний': Fore.RED,
    'синій': Fore.BLUE,
    'зелений': Fore.GREEN
}

if color in colors:
    self.color = colors[color]
else:
    raise Exception(f'Такого кольору немає: {color}')

