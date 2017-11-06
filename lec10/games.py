import random
def playCoinToss():
    print('Welcome to this game of chance!!!')
    coinSides= ['Heads', 'Tails']
    #Infinite loop - not generally good
    c ='y'
    while c=='y':
        playerChoice = input('\n\nPick a side Heads (H) or Tails (T): ')
        result = random.choice(coinSides)
        if playerChoice == result[0]:
            print('Congrats! You won!!!')
        else:
            print('Sorry better luck next time!!!')
        c = input('Do you want to continue (y/n)?')


        

    
