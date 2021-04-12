class Slime:
    name = ''
    weight = 0
    eyes = 2

    def say_brr(self):
        rs = 'r' * self.eyes
        print(f"{self.name}: B{rs}")

    def __add__(self, other):  # +
        new_slime = Slime()
        new_slime.name = self.name[:len(self.name) // 2] + other.name[len(other.name) // 2:]
        new_slime.weight = self.weight + other.weight
        new_slime.eyes = self.eyes + other.eyes
        return new_slime

    def __gt__(self, other):  # >
        return self.weight > other.weight

    def __eq__(self, other):  # ==
        return self.weight == other.weight

    def __len__(self):
        return int((self.weight / 2) ** (1/3))  # типу обчислюємо довжину майнкрафтівського слимака

    def __str__(self):  # str
        return f"😀 Слимак {self.name} (вага: {self.weight}; очей: {self.eyes})"


s1 = Slime()
s1.name = 'Sleezy'
s1.weight = 60

s2 = Slime()
s2.name = 'Breezy'
s2.weight = 40
s2.eyes = 3

s3 = Slime()
s3.name = 'Creezy'
s3.weight = 60
s3.eyes = 6

print()
