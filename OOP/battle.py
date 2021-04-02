class Hero:
    name = ''
    attack = 4
    max_hp = hp = 20
    armor = 1
    is_alive = True
    weapon = None

    def get_damage(self, damage):
        remaining_damage = damage - self.armor
        print(f'{self.name} заблокував {self.armor} урону з {damage}')
        if remaining_damage > 0:
            self.loose_hp(remaining_damage)

    def loose_hp(self, damage):
        self.hp -= damage
        print(f'{self.name} втратив {damage} hp. В нього залишилося {self.hp} / {self.max_hp} hp')
        if self.hp <= 0:
            self.die()

    def die(self):
        self.is_alive = False
        print(f'{self.name} помирає :(')

    def normal_attack(self, other):
        print(f'{self.name} атакує героя {other.name}')
        full_damage = self.attack
        if self.weapon:
            full_damage += self.weapon.attack()
        other.get_damage(full_damage)


class Weapon:
    name = ''
    damage = 0
    durability = 0
    attack_text = ''
    is_alive = True

    def attack(self):
        """
        :return: int: додатковий урон
        """
        if not self.is_alive:
            print(f'Зброя {self.name} вже зламана!')
            return 0

        self.decrease_durability()
        print(f"{self.attack_text}  (+ {self.damage} dmg)")
        return self.damage

    def decrease_durability(self):
        self.durability -= 1
        if self.durability <= 0:
            print(f'Зброя {self.name} зламалася!')
            self.is_alive = False


def battle(hero1: Hero, hero2: Hero):
    round = 1
    while hero1.is_alive and hero2.is_alive:
        print(f'\n\n----== Починається раунд {round}.')
        hero1.normal_attack(hero2)
        print('-' * 40)
        hero2.normal_attack(hero1)
        round += 1

    if hero1.is_alive:
        print(f'Виграв герой {hero1.name}')
    elif hero2.is_alive:
        print(f"Виграв герой {hero2.name}")
    else:
        print(f'Всі програли :D')


h1 = Hero()
h1.name = 'Слимак'
h1.attack = 2
h1.hp = h1.max_hp = 30
h1.armor = 2

h2 = Hero()
h2.name = 'Мечник'
h2.attack = 3
h2.hp = h2.max_hp = 18

h3 = Hero()
h3.name = 'Огр'
h3.attack = 1
h3.hp = h3.max_hp = 30
h3.armor = 2

dubina = Weapon()
dubina.name = 'Дубина'
dubina.damage = 1
dubina.durability = 1000
dubina.attack_text = 'Дубина робить Бум'

h3.weapon = dubina

sword = Weapon()
sword.name = 'Меч'
sword.damage = 3
sword.durability = 2
sword.attack_text = 'Меч робить Вжух'

h2.weapon = sword

battle(h2, h3)
