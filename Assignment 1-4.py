#Assignment 1-4
space=[int(n) for n in input().split()]
count=int(input())
car=[int(n) for n in input().split()]
car_count=[0,0,0]
ans=0
for i in range(count):
    if(car[i]>=1 and car[i]<=199):
        car_count[0]+=1
    elif(car[i]>=200 and car[i]<=499):
        car_count[1]+=1
    else:
        car_count[2]+=1
for i in range(len(car_count)):
    for j in range(i,len(car_count)):
        while(space[j]>0 and car_count[i]>0):
            space[j]-=1
            car_count[i]-=1
            ans+=1
print(ans)
