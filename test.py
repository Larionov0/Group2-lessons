lst = [1, 2, 3, 4, 5, 6, 7]


# for el in lst:
#     if el % 2 == 0:
#         lst.remove(el)

i = 0
while i < len(lst):
    el = lst[i]
    if el % 2 == 0:
        lst.remove(el)
        i -= 1
    i += 1
