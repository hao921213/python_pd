#Assignment 1-2
sum=0
count=0
while True:
    a=int(input("請輸入正整數(若輸入零或負數結束): "))
    if a<=0:
        break
    count+=1
    if count==1:
        max_num=a
        min_num=a
    sum+=a
    max_num=max(max_num,a)
    min_num=min(min_num,a)
print("共輸入 %d 個數"%(count))
print("最大數:",max_num)
print("最小數:",min_num)
print("輸入數總和為:",sum)
print("輸入數平均為: %.1f"%(float(sum/count)))
