import pickle


class Box:
    def __init__(self, name, l, w, h, fruits=None):
        self.name = name
        self.height = h
        self.width = w
        self.length = l
        if fruits is None:
            fruits = []
        self.fruits = fruits

    def __str__(self):
        return f"|Box {self.name}  ({self.fruits})|"


class Fruit:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"[{self.name} ({self.price} грн; {self.weight} г)]"

    def __repr__(self):
        return self.__str__()


b1 = Box('Korobonka', 0.5, 0.4, 0.3, [Fruit('манго', 100, 300)])
b1.fruits.append(Fruit('огірок', 10, 200))

binary_string = pickle.dumps(b1)
with open('some_file.dat', 'wb') as file:
    file.write(binary_string)

with open('some_file.dat', 'rb') as file:
    binary_string = file.read()
new_box = pickle.loads(binary_string)

print(new_box)
