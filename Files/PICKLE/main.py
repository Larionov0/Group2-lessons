import pickle

data = [
    {'a': 2, 'b': [1, 2, 3]},
    {'a': 4, 'b': [3, 2, 1]}
]


with open('file.dat', 'wb') as file:
    file.write(pickle.dumps(data))


with open('file.dat', 'rb') as file:
    struct = pickle.loads(file.read())


print(struct == data)
