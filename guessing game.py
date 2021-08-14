import random
import sys



def game(x,y,z):
    random_num = random.randint(x,y)
    shot = 0
    while shot < z:  # add you so stupid # add last call
        while True:
            try:
                num_guess = int(input(f'enter a number between {x}-{y},you have {5 - shot} shots left:\n'))
                if x <= num_guess <= y:
                    break
                else:
                    print(f'i said enter a number between {x}-{y} dimwit,again')
            except ValueError:
                print('DAMN you stupid....i said a numberrrr')
        shot += 1
        if random_num == num_guess:
            print(f'congratulations mudafaka!! {num_guess} is on the money!!')
            break
        elif num_guess > random_num:
            print(f'{num_guess} is too high mudafaka4!!')
        elif num_guess < random_num:
            print(f'{num_guess} is too low mudafaka4!!')
    while True:
        go_again = input('wanna go again? yes/no:\n ')
        if go_again == 'yes':
            game(int(x), int(y), int(z))
        elif go_again == 'no':
            print("see you next time")
            exit()


x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]
game(int(x), int(y), int(z))


