import random


class Human:
    def __init__(self, name, age, is_male, money, have_playstation=False):
        self.name = name
        self.age = age
        self.is_male = is_male
        self.money = money
        self.have_playstation = have_playstation

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


class Worker(Human):
    def __init__(self, name, age, is_male, money, job=None, have_playstation=False):
        super().__init__(name, age, is_male, money, have_playstation)
        self.job = job

    def say_hi(self):
        print(f"{self.name}: Ох блін, привіт")

    def get_salary(self, salary):
        self.money += salary
        print(f'{self.name} отримав {salary} грн .  Тепер у нього {self.money}')

    def grow_up(self):
        super().grow_up()
        self.say_smth('Нарешті, пора підвищувати зарплату!')

    def work(self):
        if self.job == 'зварщик':
            self.say_smth("*шум зварювального апарату*")
            self.get_salary(100)
        elif self.job == 'гружчик':
            self.say_smth('*пыхтит*')
            self.get_salary(70)
        elif self.job == 'програміст':
            self.say_smth('*звук клави*')
            self.get_salary(150)


class Gamer(Human):
    def __init__(self, name, age, games, is_male, money):
        self.games = games
        self.exp = 0
        super().__init__(name, age, is_male, money, True)

    def play(self):
        game = random.choice(self.games)
        self.say_smth(f'Я граю в {game}')
        self.up_exp(random.randint(10, 100))

    def up_exp(self, exp):
        self.exp += exp
        print(f"{self.name} отримав {exp} досвіду. Тепер у нього {self.exp} xp")


class ProGamer(Gamer):
    def __init__(self, name, age, games, is_male, money, team):
        super().__init__(name, age, games, is_male, money)
        self.exp = 10000
        self.team = team

    def play(self):
        super().play()
        cash = random.randint(100, 10000)
        self.money += cash
        print(f'{self.name} отримав {cash} грн. Тепер у нього {self.money} грн')


h = Human('Bob', 12, True, 100)
w = Worker('Alex', 42, True, 5000, 'гружчик', True)
g = Gamer('Katia', 52, ['Винни Пух'], False, 140)
pg = ProGamer('John', 14, ['ADS', 'gshd', 'sgdh', 'dnfh'], True, 12450, 'Cats')


pg.say_hi()
pg.grow_up()
pg.play()
