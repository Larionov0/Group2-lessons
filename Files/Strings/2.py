text = input('Введіть вираз: ')
numbers_str = text.split(' + ')
sum_ = 0
for number_str in numbers_str:
    number = float(number_str)
    sum_ += number

print(f"{text} = {sum_}")
