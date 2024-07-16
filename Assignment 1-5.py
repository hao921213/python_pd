#Assignment 1-5
result=[]
while(True):
    M=[n for n in input().split()]
    if(int(M[0])==0):
        break
    count=int(M[0])
    char=M[1]
    count1=0
    count2=int(len(char)/count)
    ans=""
    for i in range(count):
        temp=char[count1:count2]
        for j in range(1,int(len(char)/count)+1):
            ans+=temp[-j]
        count1+=int(len(char)/count)
        count2+=int(len(char)/count)
    result.append(ans)
for i in result:
    print(i)