import random
dict={ 's':1 ,'w':2,'g':3 }
dict_rev={ 1:'snake' ,2:'water',3:'gun' }
draw=0
won=0
lost=0
while True:
    computer=random.choice([1,2,3])
    while True:
        n=input('enter your choice').lower()
        if n  in dict:
         break
        print('invalid choice. enter s for snake , g for gun and w for water')
    you=dict[n]
    print(f'you chosed {dict_rev[you]} while the computer chosed {dict_rev[computer]}')
    if(computer==you):
        print('Draw')
        draw+=1
    elif((computer-you==1 )or (computer-you== -2)):
        print('you won')
        won+=1
    elif((computer-you==2 )or (computer-you== -1)):
        print('you lost')
        lost+=1
    again=input('you want to play again(y for yes , n for no)').lower()
    if again!='y':
        print('thanks for playing')
        break
print(f'the won matches are {won} , lost matches are {lost} , and draw are {draw}')






