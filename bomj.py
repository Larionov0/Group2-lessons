import random
from time import sleep


money = 1000
satiety = max_satiety = 10
satiety = 1
things = [
    ['аксесуар', 'шорти', 0],
    ['аксесуар', "кепка", 0],
    ]

store = [
        ['аксесуар', 'тапки', 50],
        ['аксесуар', "телефон", 200],
        ['аксесуар', "спортивний костюм", 300],
        ['аксесуар', "смартфон", 1000],
        ['аксесуар', 'ноутбук', 6000],
        ['аксесуар', 'квартира', 100000],
        ['їжа', 'хліб', 10, 2],
        ['їжа', 'окорок', 70, 6],
        ['їжа', 'піца з равликами', 700, 10]
    ]

print("Welcome to Симулятор Бомжа")
while True:
    if satiety <= 0:
        print("Бомж відкинув копита :(")
        break
    print("\n\n\n--= Головне меню =--")
    print("Гроші: ", money, 'грн')
    print("Ситість: ", satiety, '/', max_satiety)
    print("Речі:")
    for thing in things:
        print('-', thing[1])
    print('----= Ваші дії:')
    print("0 - вихід з гри")
    print("1 - магазин")
    print("2 - на заробітки")
    print("3 - вуличні битви")
    print("4 - поритися на звалці")
    print("5 - поїсти")
    
    choice = input("Ваш вибір: ")
    if choice == '1':
        while True:
            print("\n\n--= Магазин =--")
            print("Гроші: ", money, 'грн')
            print("Ситість: ", satiety, '/', max_satiety)
            print("Речі:")
            for thing in things:
                print('-', thing[1])
            print('----= Товари:')
            print("0 - назад")

            # Виводимо вс товари на екран
            i = 1
            for thing in store:
                print(i, '-', thing[1], '(', thing[2], 'грн )')
                i += 1

            # Користувач вибирає номер товару
            choice = int(input("Ваш вибір: "))
            if choice == 0:
                break

            # Дістаємо річ зі списку за заданим номером
            thing = store[choice - 1]  # наприклад thing = ["смартфон", 1000]

            # Стандартна логіка зі зняттям коштів (покупка)
            if money >= thing[2]:
                money -= thing[2]
                things.append(thing)
                print("Успішна закупка: ", thing[1])
            else:
                print("Недостатньо грошей:(")
            
    elif choice == '2':
        while True:
            print("\n\n--= Заробітки =--")
            print("Гроші: ", money, 'грн')
            print("Ситість: ", satiety, '/', max_satiety)
            print("Речі:")
            for thing in things:
                print('-', thing[1])
            print('----= Ваші дії:')
            print("0 - назад")
            print("1 - жебракувати (0 - 30 грн)")
            print("2 - збирати пляшки (10 - 20 грн)")
            print("3 - гружчик (потрібне взуття) (50 грн)")
            print("4 - менеджер (потрібен телефон, костюм) (200 грн)")
            choice = input("Ваш вибір: ")
            if choice == '0':
                break
            elif choice == '1':
                print("Бомж став на коліна і збирає данину...")
                sleep(3)
                zarobitok = random.randint(0, 30)
                money += zarobitok
                print("Бомж заробив", zarobitok, "грн. Тепер у нього", money, 'грн')
                satiety -= 1
            elif choice == '2':
                print("Бомж збирає пляшки...")
                sleep(3)
                zarobitok = random.randint(10, 20)
                money += zarobitok
                print("Бомж заробив", zarobitok, "грн. Тепер у нього", money, 'грн')
                satiety -= 1
            elif choice == '3':
                if ['аксесуар', 'тапки', 50] in things:
                    print("Бомж іде грузити товари")
                    print("Перетаскуємо мішки...")
                    input("<Enter>")
                    print("Тягаємо ящики...")
                    input("<Enter>")
                    print("Грузимо мішки...")
                    input("<Enter>")
                    print("Чистимо взуття начальнику...")
                    input("<Enter>")
                    
                    zarobitok = 50
                    money += zarobitok
                    print("Бомж заробив", zarobitok, "грн. Тепер у нього", money, 'грн')
                    satiety -= 2
                else:
                    print("Недостатньо речей!")
        
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        while True:
            print("--= Поїдання =--")
            print("Гроші: ", money, 'грн')
            print("Ситість: ", satiety, '/', max_satiety)
            print("Речі:")
            for thing in things:
                print('-', thing[1])
            food = []
            for thing in things:
                if thing[0] == 'їжа':
                    food.append(thing)

            # виводимо всю їжу, яка є у гравця
            print("0 - назад")
            i = 1
            for dish in food:
                print(f"{i} - {dish[1]} (+{dish[3]} ситості)")
                i += 1
            
            choice = int(input("Ваш вибір: "))
            if choice == 0:
                break

            dish = food[choice - 1]  # dish=['їжа', 'хліб', 10, 2]
            print("Бомж зїв", dish[1])
            things.remove(dish)
            satiety += dish[3]
            if satiety > max_satiety:
                satiety = max_satiety
        
    elif choice == '0':
        break
    else:
        pass
