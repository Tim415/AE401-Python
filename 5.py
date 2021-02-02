import random
num=random.randint(1,10)
i=0
while i<1:
    guess=int(input('please pick a number from one to ten'))
    if num == guess:
        print('you are right')
        i=1
    elif num<guess:
        print('your answer is too big')
    else:
        print('your answer is too small')