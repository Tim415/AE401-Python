import random
big=int(input('輸入最大上限數字'))
small=int(input('輸入最小下限數字'))
number=random.randint(small,big)
chance=int(input('輸入你想要有的機會數字'))
guesstimes=0
for i in range(chance):
    guesstimes=guesstimes+1
    guess=int(input('請猜數字'))
    if guess==number:
        print('恭喜你答對了，你花了',guesstimes,'次')
        break
    elif (guess>big or guess<small):
        print('你這小笨蛋，你猜的數字根本不在範圍內！')
        chance=chance+1
        guesstimes=guesstimes-1
    elif guess<number:
        print('太小了!你還剩',chance-guesstimes,'次')
    elif guess>number:
        print('太大了!你還剩',chance-guesstimes,'次')
    else:
        print('你這大笨蛋!你猜的根本不是數字')
        guesstimes=guesstimes-1
        chance=chance+1