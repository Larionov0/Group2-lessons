#1
f1 = lambda a : a/2

#2
f2 = lambda a : a[0].lower()

#3
print(list(map(lambda x: x[0], input('Words: ').split(' '))))

#4
cities = input('cities: ').split(' ')
numbers = input('numbers: ').split(' ')

zipped = list(zip(cities, numbers))

maxC = zipped
minC = zipped

maxList = list(map(lambda a: a[1] if a[1] > maxC[0][1] else maxC[0][1], zipped))
maxList2 = list(filter(lambda a: a[1] == max(maxList), zipped))
print(maxList2[0][0])

minList = list(map(lambda a: a[1] if a[1] < minC[0][1] else minC[0][1], zipped))
minList2 = list(filter(lambda a: a[1] == min(minList), zipped))
print(minList2[0][0])

#5
numList = input("num: ").split(' ')

normal = list(filter(lambda a: None if int(a) % 3 == 0 else a, numList))
print(normal)