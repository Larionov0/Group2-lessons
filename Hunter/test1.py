import msvcrt


def press(text):
    print(text)
    return msvcrt.getch().decode()


key = press('Натисніть на клавішу: ')
if key == 'j':
    print(True)
