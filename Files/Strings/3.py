text = input('Введіть вираз: ')
dirty_numbers_str = text.split('+')
sum_ = 0
for dirty_number_str in dirty_numbers_str:
    number_str = dirty_number_str.strip()
    number = float(number_str)
    sum_ += number

print(f"{text} = {sum_}")
