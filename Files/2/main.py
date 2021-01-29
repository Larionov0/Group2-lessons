file = open('Cities.txt', 'rt')

cities = []
for line in file:
    cities_in_line = line.rstrip().split(', ')
    cities.extend(cities_in_line)

file.close()

print(cities)
