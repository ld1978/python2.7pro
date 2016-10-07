#-*- coding:utf-8 -*-
import os
import shutil
src='e:\\d'
dst='e:\\e'
sdirs=os.listdir(src)
#print names
#os.makedirs(dst)
os.chdir(src)
all_the_text=[]
with open('find.txt','r') as f:
    for line in f:
        all_the_text.append(line.strip('\n'))
        #print line
for i in sdirs[0:-1]:
    print i
    if i in all_the_text:
        shutil.move(str(i),'e:\\e')
    else:
        print 'directory is not exists.'
            #dirname1=str(i[0])
            #dirname2=dirname1[1:]
            #dirname3=dirname2[4:]
            #print dirname
            #if i in line:
            #os.mkdir(dirname3)
                #shutil.move('e:\\d\\'+i,dst)