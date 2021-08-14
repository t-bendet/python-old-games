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
                     |___/      
                                         """)

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

    def clear_me():  # clears the screen after user input
        os.system('cls')

    while True:  # checking input is valid
        try:
            choice = input('choose a category number:\n'  # picking a a category
                           '1.movies\n'
                           '2.musicians\n'
                           '3.books\n')
            word = (random.choice(categories[choice]))  # picking a random word
            clear_me()
            break
        except KeyError:
            clear_me()
            print(f'{choice} is not a valid choice')
    correct_letters_guessed = set()
    incorrect_letters_guessed = set()

    def generate_word_string(word, letters_guessed):
        output = []
        for letter in word:
            if letter in letters_guessed:
                output.append(letter.lower())
            elif letter == " ":
                output.append("  ")
            else:
                output.append("_ ")
        return " ".join(output)

    while counter < max_tries:
        secret_word = generate_word_string(word, correct_letters_guessed)
        if word.replace(" ", "") == secret_word.replace(" ", ""):
            print(f'well done!\n'
                  f'{word} is correct!')
            break
        print(secret_word)
        print(word)
        while True:
            guess = input('pick a letter:')
            if guess in ascii_letters and len(guess) == 1:
                guess = guess.lower()
                break
            else:
                clear_me()
                print(secret_word)
                continue
        clear_me()
        if guess in correct_letters_guessed or guess in incorrect_letters_guessed:  # if the letter has been guessd already
            print(f'mmmmm... you kind\'a guessed {guess} already.\n')
        elif guess in word:
            correct_letters_guessed.add(guess)
            print('good guess')
        else:
            incorrect_letters_guessed.add(guess)
            counter += 1
            print(which_anima[counter])
            print(f'mmmmm...{guess} is not what we where looking for.')
    if counter == max_tries:
        print(f'so close...the word was {word}')
    one_more = input('would you like to play another game? yes/no?:')
    while one_more != 'yes' and one_more != 'no':
        clear_me()
        one_more = input('would you like to play another game? yes/no?:')
    if one_more == 'yes':
        clear_me()
        hangman()
    else:
        clear_me()
        print(f'thank you!bye bye now')
        exit()



hangman()
