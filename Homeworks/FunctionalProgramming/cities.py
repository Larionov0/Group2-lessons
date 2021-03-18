'''
 Написать программу, в котрой пользователь вводит города через пробел, а затем вторым 
 вводом вводит столько же чисел через пробел - количества жителей соответствующих городов.
Программа должна вывести на экран город с максимальным и минимальным количеством жителей.
Разрешено использовать только один цикл for вместе с zip. Остальную работу проделывать функцией map.
'''

cities = input('Enter cities with gap:')
people = input('Enter number of people with gap:')

cities_lst = cities.split(' ')
people_lst = people.split(' ')
people_lst_int = list(map(int, people_lst))


index_max = people_lst_int.index(max(people_lst_int))
print(people_lst_int[index_max], cities_lst[index_max])

index_min = people_lst_int.index(min(people_lst_int))
print(people_lst_int[index_min], cities_lst[index_min])
