class Slime:
    def __init__(self, name, weight, eyes=2):  # викликається при створенні нового об'єкту
        self.name = name
        self.weight = weight
        self.eyes = eyes

    def say_brr(self):
        rs = 'r' * self.eyes
        print(f"{self.name}: B{rs}")

    def __add__(self, other):  # +
        new_slime = Slime(
            name=self.name[:len(self.name) // 2] + other.name[len(other.name) // 2:],
            weight=self.weight + other.weight,
            eyes=self.eyes + other.eyes
        )
        return new_slime

    def __gt__(self, other):  # >
        return self.weight > other.weight

    def __eq__(self, other):  # ==
        return self.weight == other.weight

    def __len__(self):
        return int((self.weight / 2) ** (1/3))  # типу обчислюємо довжину майнкрафтівського слимака

    def __str__(self):  # str
        return f"😀 Слимак {self.name} (вага: {self.weight}; очей: {self.eyes})"


s1 = Slime('Sleezy', weight=60)
s2 = Slime('Breezy', weight=40, eyes=3)
s3 = Slime('Creepy', 60, 6)

print(s1 + s3)
