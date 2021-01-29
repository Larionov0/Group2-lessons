import random
from time import sleep


money = 100
satiety = max_satiety = 10
things = ['шорти', "кепка"]
food = []

print("Welcome to Симулятор Бомжа")
while True:
    print("\n\n\n--= Головне меню =--")
    print("Гроші: ", money, 'грн')
    print("Ситість: ", satiety, '/', max_satiety)
    print(things + food)
    print('----= Ваші дії:')
    print("1 - магазин")
    print("2 - на заробітки")
    print("3 - вуличні битви")
    print("4 - поритися на звалці")
    print("5 - з`їсти")
    print("0 - вихід з гри")
    
    choice = input("Ваш вибір: ")
    if choice == '1':
        while True:
            print("\n\n--= Магазин =--")
            print("Гроші: ", money, 'грн')
            print("Ситість: ", satiety, '/', max_satiety)
            print(things + food)
            print('----= Товари:')
            print("0 - назад")
            print("1 - тапки (50 грн)")
            print("2 - телефон (200 грн)")
            print("3 - спортивний костюм (300 грн)")
            print("4 - смартфон (1000 грн)")
            print("5 - окорок (30 грн)(5 ситість)")
            choice = input("Ваш вибір: ")
            if choice == '0':
                break
            elif choice == '1':
                if money >= 50:
                    money -= 50
                    things.append('тапки')
                    print("Успішна закупка")
                else:
                    print("Недостатньо грошей:(")
            elif choice == '2':
                if money >= 200:
                    money -= 200
                    things.append('телефон')
                    print("Успішна закупка")
                else:
                    print("Недостатньо грошей:(")
            elif choice == '3':
                pass
            
            elif choice == '4':
                pass
            elif choice == '5':
                if money >= 30:
                    money -= 30
                    food.append('окорок')
                    print("Успішна закупка")
                else:
                    print("Недостатньо грошей:(")
            
    elif choice == '2':
        while True:
            print("\n\n--= Заробітки =--")
            print("Гроші: ", money, 'грн')
            print("Ситість: ", satiety, '/', max_satiety)
            print(things + food)
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
                if 'тапки' in things:
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
        if 'окорок' in food:
            food.pop(0)
            satiety += 5
        else:
            print("нічого з`їсти :(")
    elif choice == '0':
        break
    else:
        pass
