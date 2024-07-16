#Lab 9-10
import random as r
while (True):
    a=input()
    if(len(a)>0):
        num=r.randint(1,6)
        print("結果為:",num)
    else:
        break

#Lab 9-11
import random as r
list=r.sample(range(1,50),7)
special=list.pop()
for i in range(6):
    if i==5:
        print(list[i])
    else:
        print(list[i],end=", ")
print("特別獎為:",special)