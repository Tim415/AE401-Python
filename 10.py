import random
big=int(input('輸入最大上限數字'))
small=int(input('輸入最小下限數字'))
number=random.randint(small,big)
chance=int(input('輸入你想要有的機會數字'))
guesstimes=0
for i in range(chance):
    guesstimes=guesstimes+1
    guess=int(input('請猜數字'))
    while (guess>big or guess<small):
        print('你這小笨蛋，你猜數字的根本不在範圍內！')
        guess=int(input('請猜數字'))
    if guess==number:
        print('恭喜你答對了，你花了',guesstimes,'次')
        break
    elif guess<number:
        print('太小了!你還剩',chance-guesstimes,'次')
        if chance-guesstimes==0:
            print('你猜的次數已經用完了，正確答案是',number)
    elif guess>number:
        print('太大了!你還剩',chance-guesstimes,'次')
        if chance-guesstimes==0:
            print('你猜的次數已經用完了，正確答案是',number)