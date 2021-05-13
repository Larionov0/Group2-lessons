from os import system
from .settings import N, M


def clear():
    system('cls')


def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


def create_matrix():
    return [['-' for _ in range(M)] for _ in range(N)]


def print_matrix(matrix):
    text = ''
    for row in matrix:
        text += '|'
        for el in row:
            text += str(el) + ' '
        text = text[:-1] + '|\n'
    print(text)

