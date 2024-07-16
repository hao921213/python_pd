#資料結構
#陣列
#一維陣列   串列名稱=[元素1,元素2,元素3,...]  可包含不同型態的元素，index從0開始
data=[1,2,3,4,5]
print(data[0])
print(data[-1])
print(data[-9])
print(data[1])
#陣列名稱[start:end:step]從start到end的前一位，間隔為step
print(data[1:7:2])
print(data[1::2])
print(data[::2])
print(data)
#改變元素的內容   陣列名稱[index]=data
#len()陣列長度，max()陣列最大值，min()陣列最小值，sum()陣列總和
print(len(data))
print(max(data))
print(min(data))
print(sum(data))
#陣列常用用法
list1=list2=list3=list4=list5=[10,20,30,40,50]
list1.append(60)#陣列.append(value) 加入value在list的最後  也可以是陣列
print(list1)
list1.extend([10,30])#陣列.extend([value1,value2...]) 加入陣列在list後 限制只能為陣列
list2.pop()#陣列.pop(index) 刪除陣列第index+1的元素，若無value則刪除最後一個元素  同時可以得到刪除的index
print(list2)
list3.pop(2)
print(list3)
list4.remove(30)#陣列.remove(value) 移除陣列第一次遇到的value值
print(list4)
list5.insert(2,70)#陣列.insert(index,value) 在第value+1的位置中加入value值
print(list5)
list=[1,2,3,4,5]
print(list.index(3))#陣列.index(value) 找到陣列中第一次出現value的index值
print(list.count(3))#陣列.count(value) 輸出value在陣列中出現幾次
#del 陣列[start:end:step] 刪除想要刪除的值
#del list[3] 刪除index=3的值
#del list[1:4] 刪除index=1-3的值
#del list[:] 刪除所有值
#陣列.clear() 清除所有值與del list[:]相同

#Lad 8-1
score=[]
sum=intotal=0
while(intotal!=-1):
    intotal=input("請輸入學生成績:")
    score.append(intotal)
score.pop()
print("總成績:%d"%(sum(score)))
print("平均:%f"%(sum(score)/len(score)))

#Lab 8-2
for x in "welcome":
    print(x," ")
else:
    print("字串以輸出完畢")

#串列產生器
list=[0 for i in range(10)]
for i in list:
    print(x,end=" ")

list=[y for y in range(10)]
for i in list:
    print(x,end=" ")

list=[(y+2) for y in range(10)]
for i in list:
    print(x,end=" ")

#Lab 8-3
list=[11,22,33,44,55,66]
print(list,end=" ")
temp=list[0]     #儲存第一個變數
for i in range(len(list)):
    if(i<len(list)-1):
        list[i]=list[i+1]#把變數往前移
    else:
        list[i]=temp#新的陣列的最後一個變數放舊的第一個變數
print(list,end=" ")

#Lab 8-4
list=[0 for i in range(5)]
for i in range(len(list)):
    temp=int(input("請輸入數字:"))
    list[i]=temp
print("平均為:%d"%(sum(list)/len(list)))

#Assignment 1-5(未檢查)
M=[int(n) for n in input().split()]
count=M[0]
char=M[1]
count1=0
count2=count
for i in range(len(char)/count):
    ans+=char[count2:count1]
    count1+=count
    count2+=count
print(ans)
