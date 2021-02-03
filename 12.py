people=int(input('our class have how many people?'))
scores=[]
distance=[]
time=-1
max=0
min=101
averagescore=0
averageage=0
for i in range(people):
    aperson=list()
    time=time+1
    name=str(input("that student's name"))
    aperson.append(name)
    score=int(input("one of our student's score"))
    aperson.append(score)
    age=int(input("that student's age"))
    aperson.append(age)
    averagescore=(averagescore+score)/people
    averageage=(averageage+age)/people
    scores.append(aperson)
    if score>max:
        max=scores[time][1]
        maxname=scores[time][0]
        maxage=scores[time][2]
    if score<min:
        min=scores[time][1]
        minname=scores[time][0]
        minage=scores[time][2]
time=-1
for i in range(people):
    time+1
    score=scores[time][1]
    if averagescore>score:
        distance[time]=averagescore-score
    else:
        distance[time]=score-averagescore
nearscore=(min(distance))
nearage=(min(distance))
print('分數最高的分數是',max,'他的名子是',maxname,'他的年齡是',maxage,'歲,分數最低的分數是',min,'他的名子是',minname,'他的年齡是',minage,'歲,平均分數是',averagescore,'平均年齡是',averageage,'歲,最接近平均分數的人是',scores[nearscore][0],'他的分數是',scores[nearscore][1],'最接近平均年齡的人是',scores[nearage][0],'他的年齡是',scores[nearage][1])
print(scores)