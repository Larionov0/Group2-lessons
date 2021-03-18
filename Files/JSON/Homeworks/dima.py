import json

SAVINGS_FILENAME = 'savings.json'

roomTest = {
    'number': 0,
    'width': 0,
    'length': 0,
    'price': 0,
    'canHold': 0,
    'held': 0,
    'items': {'wardrobe': 0, 'tv': 0, 'table': 0, 'chair': 0}
}


def create_data():
    data = []
    return data


def save_data(data):
    with open(SAVINGS_FILENAME, 'wt', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))


def load_data():
    with open(SAVINGS_FILENAME, 'rt', encoding='utf-8') as file:
        data = json.loads(file.read())
    return data


def try_to_load_data():
    try:
        return load_data()
    except Exception as ex:
        print('Сталася помилка з файлом збереження:')
        print(ex)
        print('Створюємо нові дані')
        input('<Enter>')
        return create_data()


def RoomInput(string):
    roomInput = int(input((string + ": ")))
    return roomInput


def main():
    data = try_to_load_data()
    while True:
        print("---Main Menu---")
        print("1 - create/delete room")
        print("2 - search room")
        print("3 - add guests")
        print("4 - statistics")
        print("5 - exit")
        print("6 - print data")
        playerInput = int(input("Input: "))
        if playerInput == 5:
            break
        if playerInput == 1:
            print(FirstTask(data))
        if data != []:
            if playerInput == 2:
                print(SecondTask(data))
            elif playerInput == 3:
                ThirdTask(data)
            elif playerInput == 4:
                ForthTask(data)
            elif playerInput == 6:
                print(data)
        else:
            print("add some rooms!")
        save_data(data)


def FirstTask(data):
    room = {
        'number': 0,
        'width': 0,
        'length': 0,
        'price': 0,
        'canHold': 0,
        'held': 0,
        'items': {'wardrobe': 0, 'tv': 0, 'table': 0, 'chair': 0}
    }
    playerChoice = int(input("create/delete room?(1/2): "))
    if playerChoice == 1:
        keys = list(room.keys())
        itemsKeys = list(room['items'].keys())
        print(keys)
        i = 0
        while i < len(room) - 1:
            roomInput = RoomInput(keys[i])
            room[keys[i]] = roomInput
            i += 1
        i = 0
        while i < len(itemsKeys):
            itemInput = RoomInput(itemsKeys[i])
            item = itemsKeys[i]
            room['items'][item] = itemInput
            i += 1
        data.append(room)
        return room
    else:
        Index = int(input("delete room by number: "))
        i = 0
        while i < len(data):
            if data[i]['number'] == Index:
                data.pop(i)
            i += 1
        return None


def SecondTask(data):
    roomList = []
    areaInput = int(input("Area: "))
    canHoldInput = int(input("Guests: "))

    for room in data:
        if room['width'] * room['length'] >= areaInput and room['canHold'] >= canHoldInput:
            roomList.append(room['number'])
    return roomList


def ThirdTask(data):
    numInput = int(input("Room number: "))
    guestsInput = int(input("Guests number: "))
    a = 0

    for room in data:
        if room['number'] == numInput:
            if guestsInput <= room['canHold'] - room['held']:
                room['held'] += guestsInput
                print('check in succesful')
                a += 1
    if a != 1:
        print('sorry, no such places')


def ForthTask(data):
    canHold = 0
    held = 0
    area = 0
    items = {'wardrobe': 0, 'tv': 0, 'table': 0, 'chair': 0}
    price = 0

    for room in data:
        canHold += room['canHold']
        held += room['held']
        area += room['width'] * room['length']
        price += room['price']
        itemsKeys = list(items.keys())
        i = 0
        while i < len(itemsKeys):
            items[itemsKeys[i]] += room['items'][itemsKeys[i]]
            i += 1

    print(canHold)
    print(held)
    print(area)
    print(items)
    print(price)


main()
