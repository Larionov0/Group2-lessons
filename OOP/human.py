import random


class Human:
    name = 'Bob'
    age = 0
    is_male = True

    def say_hi(self):
        print(f'{self.name}: Hello')

    def say_smth(self, text):
        print(f'{self.name}: {text}')

    def grow_up(self):
        self.age += 1
        if self.is_male:
            print(f'{self.name} підріс на рік. Тепер йому {self.age} років')
        else:
            print(f'{self.name} підросла на рік. Тепер їй {self.age} років')


h1 = Human()
h1.name = 'Marina'
h1.age = 20
h1.is_male = False

h2 = Human()
h2.name = 'Vasya'
h2.age = 25

h3 = Human()
h3.age = 14


h1.grow_up()
h2.grow_up()
