from .. import settings


def perimetr(a, b):
    return a * 2 + b * 2


def authorise():
    print(settings.login)
    print(settings.password)
