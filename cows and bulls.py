import random


def game():
    game_number = str(random.randint(1000, 9999))
    cow = 0
    bulls = 0
    num_guesses = 0
    print('Welcome to the Cows and Bulls Game!')
    while True:
        num_guesses += 1
        while True:
            user_choice = (input('Enter a 4-digit number:\n'))
            if len(user_choice) == len(game_number) and user_choice.isnumeric():
                break
            else:
                print("look at the instructions again")
        if user_choice == game_number:
            print(f'well done\n'
                  f'it took you {num_guesses} attempts to guess the number\n'
                  f'would you like to play another game?:yes/no')
            another_one = input()
            if another_one == 'yes':
                game()
            elif another_one == 'no':
                print('bye bye')
                break
        elif not set(user_choice).isdisjoint(set(game_number)):  # checks if at least one of the numbers was right
            for i in range(4):
                if user_choice[i] in game_number:
                    if user_choice[i] == game_number[i]:
                        cow += 1
                    else:
                        bulls += 1
            print(f"you have {bulls} bulls and {cow} cow's ")
            bulls = 0
            cow = 0
        else:
            print('keep guessing')


game()
