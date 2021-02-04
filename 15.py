import sys
ap=[]
bpts=[]
i=0
time=0
print('這台機器有以下幾個功能')
print('1.設定')
print('2.進貨')
print('3.出貨')
print('4.營業額統計')
print('5.離開')
st=0
gp=0
pr=0
bu=0
sel=0
oots=0
now=0
while True:
    se=int(input('請選擇你要使用的功能，請2~4輪流使用'))
    if se==1:
        st=int(input('最初有幾個蘋果'))
        ap.insert(st,0)
        gp=int(input('進貨一個蘋果多少錢'))
        ap.insert(pr,1)
        pr=int(input('售價訂多少'))
        ap.insert(pr,2)
        now=now+st
    elif se==2:
        bu=int(input('今天進貨多少個蘋果'))
        now=now+bu
        ap.insert(bu,3)
        print('目前總共有',now,'顆蘋果')
        now=now+bu
    elif se==3:
        sel=int(input('總共賣出多少蘋果'))
        now=now-sel
        a=pr*sel
        print('目前還剩',now,'顆蘋果，營利',a,'元，利潤是',pr*sel-gp*sel,'元')
    elif se==4:
        while True:
            time=time+1
            oots=int(input('請輸入其中一筆交易的蘋果數量，若完成請輸入11111111這個數字'))
            if oots==11111111:
                break
            else:
                bpts.append(oots)
                print('第',time,'筆交易數量的營利是',oots*pr,'利潤是',oots*pr-gp*oots)
    elif se==5:
        fo=open('老闆好笨.txt','w')
        fo.write('今日營業額是')
        fo.close()
        fo=open('老闆好笨.txt','a')
        fo.write(str(a))
        fo.write('元。\n')
        fo.write('剩下')
        fo.write(str(now))
        fo.write('顆蘋果')
        fo.close()
        sys.exit(0)
    else:
        print('你打錯了，請重新輸入')
        s=int(input('請選擇你要使用的功能'))