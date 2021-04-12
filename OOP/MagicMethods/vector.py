class Vector:
    coords = [1, 1]

    def __add__(self, other):  # [1, 1]   [2, 5]  ->   [3, 6]
        new_vector = Vector()
        new_vector.coords = [self.coords[0] + other.coords[0], self.coords[1] + other.coords[1]]
        return new_vector

    def __mul__(self, koef):
        new_vector = Vector()
        new_vector.coords = [self.coords[0] * koef, self.coords[1] * koef]
        return new_vector


v1 = Vector()
v1.coords = [5, 5]

v2 = Vector()
v2.coords = [1, 2]


v3 = v1 + v2  # те ж саме, що і     v3 = v1.__add__(v2)
v4 = v2 * 3


print(v3.coords)
print(v4.coords)
