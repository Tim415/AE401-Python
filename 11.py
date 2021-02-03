people=int(input('our class have how many people?'))
scores=list()
time=-1
max=0
min=101
av=0
for i in range(people):
    time=time+1
    score=int(input("one of our student's score"))
    scores.append(score)
    av=av+score
    if score>max:
        max=score
    if score<min:
        min=score
print('分數最高的分數是',max,',分數最低的分數是',min,'平均值是',av/people,)