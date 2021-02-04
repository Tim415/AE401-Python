fo=open('myfile.txt','w')
fo.write('This is a test')
fo=open('myfile.txt','r')
fo=open('myfile.txt','a')
fo.close()
import os.path
if os.path.isfile('myfile.txt'):
        print('檔案存在')
else:
        print('檔案不存在')