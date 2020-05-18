import random

def userchoice():
    comp = random.choice(['Rock', 'Paper', 'Scissors'])
    print('welcome to this Rock Paper Scissors game game.Play with me\n')
    print('To play you choose \nr for rock\np for paper \ns for scissors')

    print(comp)

    user = input("Give your input and lets see if you win\n")
    if (user == 'r'):
        userinput = 'Rock'
    elif(user == 'p'):
        userinput = 'Paper'
    else:
        userinput = 'Scissors'

    if (comp == 'Rock'):
        if (userinput != 'Rock'):
            if (userinput == 'Paper'):
                print('Paper wins.You win.')
            else:
                print('I win. Youpiiii!!!!!!!!')
        else:
            print('Game null, we made the same choice')
    elif (comp == 'Paper'):
        if (userinput != 'Paper'):
            if (userinput == 'Scissors'):
                print('Scissors win.You win.')
            else:
                print('I win. Youpiiii!!!!!!!!')
        else:
            print('Game null, we made the same choice')
    else:
        if (userinput != 'Scissors'):
            if (userinput == 'Rock'):
                print('Rock win.You win.')
            else:
                print('I win. Youpiiii!!!!!!!!')
        else:
            print('Game null, we made the same choice')


userchoice()


