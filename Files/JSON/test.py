import json


data = [
    {'a': 2, 'b': [1, 2, 3]},
    {'a': 4, 'b': [3, 2, 1]}
]

string = json.dumps(data)

struct = json.loads(string)

print(struct)
