import random

vlad_options = ["my dead cat", "my pet bear",
                "my babushka", "the first kgb officer i killed",
                "my favorite vodka"]

def game():
    game_options = ["rock", "paper", "scissors"]
    again_choise = (f'rock paper or scissors!\n'
                    f'raz! dva! tri!:')
    wrong_choise = ('i said no cheating! only rock paper or scissors\n'
                    'we go again! raz! dva! tri!:')
    same_choise = (f'oh this is where i draw the line!\n'
                   f'got it?!\n'
                   f'i make joke' )
    user_win = (f'as graet americansci actor, robert de pachino say\n'
                   f'you!! your good you!')
    vlad_win = (f'Winning isn’t everything {user_name}, it’s the only thing')
    ans = input(f'o.k {user_name} on count of three we choose \n'
                f'rock papaer or scissors ! no cheating!\n'
                f'raz! dva! tri!:')
    vlad_num_wins = 0
    user_num_wins = 0
    draw_num = 0
    go_again = True
    while go_again:
        while ans not in game_options:
            print(wrong_choise)
            ans = input()
            continue
        vlad_choise = random.choice(game_options)
        vlad_win_scenrio = (ans == "scissors" and vlad_choise == "rock") or \
                           (ans == "rock" and vlad_choise == "paper") or \
                           (ans == "paper" and vlad_choise == "scissors")
        user_win_scenrio = (ans == "paper" and vlad_choise == "rock") or \
                           (ans == "scissors" and vlad_choise == "paper") or \
                           (ans == "rock" and vlad_choise == "scissors")
        if ans == vlad_choise:
            draw_num += 1
            print(f'vlad choose:{vlad_choise}')
            print(same_choise)
        if vlad_win_scenrio:
            vlad_num_wins +=1
            print(f'vlad choose:{vlad_choise}')
            print(vlad_win)
        if user_win_scenrio:
            user_num_wins +=1
            print(f'vlad choose:{vlad_choise}')
            print(user_win)
        ans = input('we go again or you had enough?:again\exit?')
        mumbling = True
        while mumbling:
            if ans == "again":
                go_again = True
                mumbling = False
                print(again_choise)
                ans = input()
            elif ans == "exit":
                mumbling = False
                go_again = False
            else:
                print('what are you mumbling over there?:again\exit?')
                ans = input()

    print(f'good game comrade {user_name} now lets see results:\n'
          f'vlad won {vlad_num_wins} games\n'
          f'{user_name} won {user_num_wins} games\n'
          f'there was {draw_num} draws')

user_name = input(f'hello there! i\'m vladimir the great,' "\n"
                  f'i am rock paper scissors champion of the USSR!!' "\n"
                  f'what is your name coomrade?')
we_play = input(f'ohhhh {user_name} is name of {random.choice(vlad_options)},\n'
                f'this is a good sign! you must now play game with me!\n'
                f'what say you? yes/no:')
if we_play == "yes":
    game()
else:
    reconsider = input('my friend..., it is not in your best interest to decline my offer\n'
                       'here in russia it is considerd... bad manner, but no worrie, you can reconsider\n'
                       'what....say....yoouu ... coomrade!:yes\yes ')
    if reconsider:
        print(f'wise choise {user_name} now we play!!')
        game()


