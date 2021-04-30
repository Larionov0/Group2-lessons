class Hero:
    class_ = 'Hero'

    def __init__(self, name, hp, attack, armor, magic, is_alive=True):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.armor = armor
        self.magic = magic
        self.is_alive = is_alive

    def get_damage(self, damage):
        if self.is_alive:
            sum_damage = damage - self.armor
            if sum_damage > 0:
                self.hp = self.hp - sum_damage
            if self.hp <= 0:
                self.die()

    def die(self):
        self.is_alive = False
        print(f'{self.name} is dead')

    def normal_attack(self, other):
        other.get_damage(self.attack)

    def cast_skill(self, other):
        pass

    def __str__(self):
        if self.is_alive:
            return (
                f'[{self.class_}] name - {self.name}, hp - {self.hp}, attack - {self.attack}, armor - {self.armor}, magic - {self.magic}')
        else:
            return (f'{self.name} is dead')


class Hunter(Hero):
    class_ = "Hunter"

    def __init__(self, name, hp, attack, armor, magic, is_alive=True):
        super().__init__(name, hp, attack, armor, magic, is_alive)

    def cast_skill(self, other):
        print(f'*{self.name} makes double attack*')
        for _ in range(2):
            other.get_damage(self.attack)


class Mage(Hero):
    class_ = 'Mage'

    def __init__(self, name, hp, attack, armor, magic, is_alive=True):
        super().__init__(name, hp, attack, armor, magic, is_alive)

    def cast_skill(self, other):
        other.get_damage(self.attack + self.magic)
        self.magic -= 5


class White_mage(Mage):
    def __init__(self, name, hp, attack, armor, magic, is_alive=True):
        super().__init__(name, hp, attack, armor, magic, is_alive)

    def cast_skill(self, other):
        self.hp += 1
        other.get_damage(self.attack + self.magic // 2)


class Black_mage(Mage):
    def __init__(self, name, hp, attack, armor, magic, is_alive=True):
        super().__init__(name, hp, attack, armor, magic, is_alive)

    def cast_skill(self, other):
        other.magic -= other.magic // 2
        self.magic += other.magic
        other.get_damage(self.attack + self.magic // 3)


class Archer(Hero):
    class_ = 'Archer'

    def __init__(self, name, hp, attack, armor, magic, is_alive=True):
        super().__init__(name, hp, attack, armor, magic, is_alive)

    def cast_skill(self, other):
        damage_ = self.attack + other.armor
        other.get_damage(damage_)
