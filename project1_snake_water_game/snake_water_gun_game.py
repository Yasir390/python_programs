import random

'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1,0,1])

myChoice = input('Enter your choice: ')
myDict = {'s':1,'w':-1,'g':0}
reverseDict = {1:'snake',-1:'water',0:'gun'}

me = myDict[myChoice]

print(f'You chose {reverseDict[me]}\n Computer chose {reverseDict[computer]}')

if(computer == me):
    print('its a draw')

else:
    if(computer == -1 and me == 1):
        print('You win!')
    elif(computer == -1 and me == 0):
        print('You lose!')
    
    elif(computer == 1 and me == -1):
        print('You lose!')
    
    elif(computer == 1 and me == 0):
        print('You win!')
    
    elif(computer == 0 and me == -1):
        print('You win!')
    
    elif(computer == 0 and me == 1):
        print('You lose!')
    else:
        print('something went wrong')
    