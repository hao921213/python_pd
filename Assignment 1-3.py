#Assignment 1-3
total=0
num=[10,11,12,13,14,15,16,17,34,18,19,20,21,22,35,23,24,25,26,27,28,29,32,30,31,33]
code=input("請輸入身分證字號:")
first_num=num[ord(code[0])-65]
total+=(first_num%10)*9+(first_num//10)
count=8
for i in range(len(code)-2):   
    total+=int(code[i+1])*count
    count-=1
total+=int(code[-1])
if(total%10==0):
    print("real")
else:
    print("fake")
