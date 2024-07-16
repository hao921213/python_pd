#Lab 4-1
pw=input("請輸入密碼:")
if(pw==1234):
    print("歡迎光臨")

#多項判斷式
'''
if 條件一:
    程式區塊一
elif 條件二:
    程式區塊二
elif 條件三:
    程式區塊三
else:
    程式區塊四
'''

#Lab 4-4
score=int(input("請輸入成績:"))
if(score>=90):
    print("優等")
elif(score>=80):
    print("甲等")
elif(score>=70):
    print("乙等")
elif(score>=60):
    print("丙等")
else:
    print("丁等")

#Lab 4-5

y=int(input("請輸入年收入(單位萬):"))
if(y<60):
    print("免繳所得稅:")
elif(y<128):
    print("所得稅為:",y*10000*0.12)
elif(y<480):
    print("所得稅為:",y*10000*0.2)
else:
    print("所得稅為:",y*10000*0.4)


#計數迴圈
#range([初始值,]終止值[,間隔值])  []為可省略   如果從大到小要記得間隔值不可忽略否則會無效
#for迴圈
#for 變數 in 串列:
#   程式區塊
    
count=0
for x in range(-3,4):
    print(x,end=" ")
    count+=1
print(count)

#Lab 5-1
a1=eval(input("請輸入首項:"))
d=eval(input("請輸入公差:"))
an=eval(input("請輸入末項:"))
n,sum=0,0
for i in range(a1,an,d):
    n+=1
    sum+=i
print("項數:",n)
print("總和:",sum)


for i in range(1,21):
    if i%2==0:
        print(i,end=" ")


#Lab 5-2
num=int(input("請輸入1-10的數:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
    if i<num:
        print(i, end="*")
    else:
        print(i,end="=")
print(fact)

#Lab 5-3
y=0
print("x^2+3x-15=y")
for i in range(1,6):
    y=i*i+3*i-15
    print("x=%d y=%d"%(i,y))

# Lab 05-A
y=0
print("3x+2=y")
for i in range(1,6):
    print("x=%d y=%d"%(i,3*i+2))
    y+=3*i+2
print(y)

#while 條件式:    else的部分不一定要有
#   程式區塊
#else:
#   敘述區段
num=0
n=1
while n<=100:
    num+=n
    n+=1
print(num)

#Lab 6-1
money=80
km=int(input("請輸入里程數:"))
km-=1.5
while(km>0):
    money+=5
    km-=0.25
print(money)


password=""
while password!="Python":
    password=input()
else:
    print(password+"is good")

#continue
for i in range(1,12):
    if(i==6):
        continue
    print(i,end=" ")


i=1
while i<26:
    if i%7!=0:
        continue
    else:
        print(i)
    i+=1

#break
for i in range(1,12):
    if(i==6):
        break
    print(i,end=" ")

#巢狀迴圈
num=0
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')

#Lab 7-2
row=6
a=1
while row>0:
    for i in range(row,0):
        print(" ")
    for j in range(1,a+1):
        print(" A")
    a+=1
    row-=1

#Lab 7-A
for i in range(1,10):
    for j in range(1,10):
        print("%d * %d ="%(i,j),i*j,end='   ')
    print()

#Assignment 1-2
print("請輸入正整數:")
a=int(input())
min_num=a
max_num=a
sum=a
if a==0:
    count=0
else:
    count=1
while a>0:
    sum+=a
    max_num=max(max_num,a)
    min_num=min(min_num,a)
    count+=1
    print("請輸入正整數:")
    a=int(input())
print("共輸入%d個數"%(count))
print("最大數=",max_num)
print("最小數=",min_num)
print("總和=",sum)
print("平均=%.1f"%(float(sum/count)))








