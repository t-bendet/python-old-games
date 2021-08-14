import random
import string
import os

HANGMAN_ASCII_ART = ("""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                          """)

print(HANGMAN_ASCII_ART)


def hangman():
    ascii_letters = string.ascii_letters
    max_tries = 6
    counter = 0
    animation_1 = ("""
    x-------x
    |
    |
    |
    |
    | """)
    animation_2 = ("""
    x-------x
    |       |
    |       0
    |
    |
    |  """)
    animation_3 = ("""
    x-------x
    |       |
    |       0
    |       |
    |
    | """)
    animation_4 = ("""
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |  """)
    animation_5 = ("""
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |  """)
    animation_6 = ("""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""")
    which_anima = {
        1: animation_1,
        2: animation_2,
        3: animation_3,
        4: animation_4,
        5: animation_5,
        6: animation_6,
    }
    categories = {
        '1': ["lord of the rings", "inception", "the prestige"],  # movies
        '2': ["eric clapton", "miles davis", "wiz khalifa"],  # musicians
        '3': ['angels and demons', 'the hobbit', 'the little prince']  # books
    }
    choice = input('choose a category number:\n'  # picking a a category
                   '1.movies\n'
                   '2.musicians\n'
                   '3.books\n')

    def clear_mr():  # clears the screen after user input
        os.system('cls')

    clear_mr()
    while choice not in '123':
        clear_mr()
        print(f'{choice} is not a valid option, '
              f'try again:')
        choice = input('choose a category number:\n'
                       '1.movies\n'
                       '2.musicians\n'
                       '3.books\n')
    clear_mr()
    word = (random.choice(categories[choice]))
    secret_word = ''
    found = []
    for char in word:
        if char == ' ':
            secret_word += '  '
        else:
            secret_word += '_ '
    print(secret_word)
    guess = input('pick a letter:')
    game = True
    while game:
        clear_mr()
        while guess not in ascii_letters or len(guess) > 1:
            guess = input(f'{guess} is not a valid choise\n '
                          f'pick a letter:')
        guess = guess.lower()
        if guess in word and guess not in found:
            found += guess
            secret_word = ''
            for item in word:
                if item == ' ':
                    secret_word += '  '
                elif item in found:
                    secret_word += item + ' '
                else:
                    secret_word += '_ '
            if word.replace(" ", "") == secret_word.replace(" ", ""):
                clear_mr()
                print(f'well done!\n'
                      f'{word} is correct!')
                one_more = input('would you like to play another game? yes/no?:')
                mumble = True
                while mumble:
                    clear_mr()
                    if one_more == 'yes':
                        hangman()
                    elif one_more == 'no':
                        mumble = False
                        game = False
                        print(f'thank you!bye bye now')
                        break
                    else:
                        one_more = input(f'{one_more} is not a valid choise\n '
                                         f'yes/no?:')



            else:
                clear_mr()
                guess = input(f'good guess!\n'
                              f'{secret_word}\n'
                              f'pick another letter:')
        elif guess in word and guess in found:
            clear_mr()
            guess = input(f'mmmmm... you kind\'a guessed {guess} already.\n'
                          f'{secret_word}\n'
                          f'pick another letter:')

        else:
            clear_mr()
            counter += 1
            if counter < max_tries:
                print(which_anima[counter])
                guess = input(f'mmmmm...{guess} is not what we where looking for.\n'
                              f'{secret_word}\n'
                              f'pick another letter:')
            else:
                print(which_anima[6])
                print('ohhh so close...')
                one_more = input('would you like to play another game? yes/no?:')
                mumble = True
                while mumble:
                    clear_mr()
                    if one_more == 'yes':
                        hangman()
                    elif one_more == 'no':
                        mumble = False
                        game = False
                        print(f'thank you!bye bye now')
                        break
                    else:
                        one_more = input('would you like to play another game? yes/no?:')


hangman()
