import msvcrt
import json
from os import system
import random


def press(text=''):
    print(text)
    return msvcrt.getch().decode()


def clear():
    system('cls')


def print_message(text=''):
    print(text)
    input('<ENTER>')


def load_words():
    '''
    return: words  (dict)
    '''
    with open('words.json', 'r', encoding='utf-8' ) as file:
        words = json.load(file)
        return words


def loading_users():
    users = [{
        'name': 'test',
        'completed_words': {},
        'successful_words': 0,
        'failed_words': 0
    }]
    with  open('users.json', 'w', encoding='utf-8') as file:
        json.dump(users, file)
    return users


def try_load_users():
    try:
        users = load_users()
        return users
    except:
        print_message('\n[Error] loading users...')
        users = loading_users()
        return users


def load_users():
    with  open('users.json', 'r', encoding='utf-8') as file:
        users = json.load(file)
        return users


def check_user(name, users):
    '''
    return: user (dict)
    '''
    for user in users:
        if user['name'] == name:
            return user
    

def from_ua_to_eng(user, words, users):
    keys_lst = []
    for key in words:
        keys_lst.append(key)
    while True:
        word = random.choice(keys_lst)
        
        if words[word] not in user['completed_words']:
            clear()
            print('[Game]===>\n')
            print('Exit - /stop')
            print(f'Translate - {words[word]}')
            ent = input(':')
            if ent == word:
                print('Nice!')
                print('[N] - Next word')
                print('[A] - Add to the study ')
                print('[B] - break')
                user['successful_words'] += 1
                ent = press()

                if ent == 'a':
                    user['completed_words'][word] = words[word]
                    save(users, 'users.json')
                elif ent == 'b':
                    return
            elif ent == '/stop':
                save(users, 'users.json')
                return
            else:
                print(f'Nope, right answer - {word}')
                print('[N] - Next word')
                print('[B] - break')
                user['failed_words'] += 1
                ent = press(':')

                if ent == 'b':
                    save(users, 'users.json')
                    return


def from_eng_to_ua(user, words, users):
    keys_lst = []
    for key in words:
        keys_lst.append(key)
    while True:
        word = random.choice(keys_lst)
        
        if words[word] not in user['completed_words']:
            clear()
            print('[Game]===>\n')
            print('Exit - /stop')
            print(f'Translate - {word}')
            ent = input(':')
            if ent == words[word]:
                print('Nice!')
                print('[N] - Next word')
                print('[A] - Add to the study ')
                print('[B] - break')
                user['successful_words'] += 1
                ent = press()

                if ent == 'a':
                    user['completed_words'][word] = words[word]
                    save(users, 'users.json')
                elif ent == 'b':
                    return
            elif ent == '/stop':
                save(users, 'users.json')
                return
            else:
                print(f'Nope, right answer - {words[word]}')
                print('[N] - Next word')
                print('[B] - break')
                user['failed_words'] += 1
                ent = press(':')

                if ent == 'b':
                    save(users, 'users.json')
                    return




def play(words, user, users, name):
    if user == None:
        user = choose_user(users, name)
    while True:
        clear()
        print('[Choose Regime]===>\n')
        print('[1] - From Ua to Eng')
        print('[2] - From Eng to Ua')
        print('[B] - Back')

        ent = press(':')

        if ent == '1':
            from_ua_to_eng(user, words, users )
        elif ent == '2':
            from_eng_to_ua(user, words, users)
        elif ent == 'b':
            return


def save(data, file_name):
    with open(file_name, 'wt', encoding='utf-8') as file:
        json.dump(data, file)



def finish_user(users, name):
    user = {}
    user['name'] = name
    user['completed_words'] = {}
    user['successful_words'] = 0
    user['failed_words'] = 0
    users.append(user)

    print_message('New user successfully created =D')


def create_user(users):
    name = ''
    while True:
        clear()
        print('[New User]===>')
        print(f'name - {name}\n')
        print('[1] - Enter name')
        print('[2] - Finish create')
        print('[B] - Back')
        
        ent = press()

        if ent == '1':
            name = input(':')
        elif ent == '2':
            finish_user(users, name)
            save(users, 'users.json')
            return
        elif ent == 'b':
            return
def choose_user(users, name=''):
    
    while True:
        clear()
        print('[Choose user]===>\n')
        print(f'name| {name}\n')
        print('[1] - Enter name')
        print('[2] - Finish')
        print('[3] - New user')
        print('[B] - back')

        ent = press()

        if ent == '1':
            name = input(':')
        elif ent == '2':
            try:
                user = check_user(name, users)
                if user != None:
                    print_message('Loading user...')
                    return user
                else:
                    print_message('Something wrong, please try again :D')
                
            except:
                print_message('Something wrong, please try again :D')
        elif ent == '3':
            create_user(users)
        elif ent == 'b':
            return


def show_completed_words(user):
    while True:
        clear()
        print('[Completed Words]===>\n')
        for word in user['completed_words']:
            print(f'{word} - {user["completed_words"][word]}')
        print('\n[B] - Back')
        ent = press()

        if ent == 'b':
            return

def show_stats(user, users):
    if user == None:
        user = choose_user(users)
    while True:
        clear()
        
        print('[Statistics]===>\n')
        print(f'name - {user["name"]}')
        print(f'successful words - {user["successful_words"]}')
        print(f'failed words - {user["failed_words"]}\n')
        print('[1] - Show completed words')
        print('[B] - Back')

        ent = press(':')

        if ent == '1':
            show_completed_words(user)
        elif ent == 'b':
            return


def main_menu(words, users, user):
    
    while True:
        clear()
        print('[Main Menu]===>')
        print(f'User - [{user["name"]}]\n')
        print('[1] - Play')
        print('[2] - Choose user')
        print('[3] - Show statistics')
        print('[0] - Exit')

        ent = press()

        if ent == '1':
            name = user["name"]
            play(words, user, users, name)

        elif ent == '2':
            user = choose_user(users, name)
            try:
                name = user['name']
            except:
                name = ''

        elif ent == '3':
            show_stats(user, users)

        elif ent == '0':
            exit()



def main():
    words = load_words()
    users = try_load_users()
    user = choose_user(users)
    main_menu(words, users, user)
    
main()