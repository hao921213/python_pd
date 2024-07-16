#二維陣列
list=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(list)
print(list[0])
print[list[0][2]]
for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j],end=" ")
    print("")

#用串列產生器產生一個串列
A=[1 for i in range(2)]
print(A)
B=[A for i in range(3)]
print(B)

#Lab 8-6
print("姓名\t底薪\t加班費\t勞健保\t實發金額")
list=[["李天德",30000,2000,1200],["許立旺",40000,3000,2400]]
result=["合計"]
for i in range(len(list)):
    list[i].append(list[i][1]+list[i][2]-list[i][3])
for i in range(1,len(list[0])):
    result.append(list[0][i]+list[1][i])
list.append(result)
for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j],end="\t")
    print()

#Lab 8-7
M=[4][3]
for i in range(4):
    M[i]=[int(n) for n in input().split()]
for i in range(4):
    for j in range(3):
        print(M[j][3-i],end=" ")
    print("")

#Lab 8-8
arrayA=[[1,2,3],[4,5,6]]
arrayB=[[1,2],[3,6],[4,2]]
arrayC=[[0 for n in range(len(arrayA))] for n in range(len(arrayB[0]))]
for i in range(len(arrayA)):
    for j in range(len(arrayB[0])):
        current=0
        for k in range(len(arrayB)):
            current+=arrayA[i][k]*arrayB[k][j]
        arrayC[i][j]=current
print(arrayC)

#Lab 8-B
numbers=[21,4,35,1,8,7,3,6,9]
odd_numbers=[]
even_numbers=[]
for i in range(len(numbers)):
    if(numbers[i]%2!=0):
        odd_numbers.append(numbers[i])
    else:
        even_numbers.append(numbers[i])
odd_numbers.sort()
even_numbers.sort(reverse="True")
print(odd_numbers)
print(even_numbers)

#turple(元素1,元素2,元素3....)與陣列不同處在於turple的值與大小不能改變
turple=(1,2,3,4)

#turple與list可以互換
turple=(1,2,3)
list=list(turple)

list=[1,2,3,4]
turple=turple(list)

#字典dic
dic={"apple":1,"banana":2,"orange":3} #dic{"鍵1":值1,"鍵2":值2,"鍵3":值3....}
print(dic["apple"]) #dic取值的index為鍵
dic["grape"]=4 #新增新的鍵與值，若鍵已存在則把原值更新為新的值
del dic["grape"] #刪除特定鍵
del dic #刪除整個dic
dic.clear() #清空dic，與del dic相同
#鍵 in dic 檢查鍵是否在dic裡
#dic.items() 取得以鍵-值組為元素組的組合
#dic.keys() 取得鍵
#dic.values() 取得值
#n=dic.get(鍵[,預設值]) 可取得「鍵」對應的「值」
#1.「鍵」存在，不論是否設定「預設值」，皆傳回字典中對應的「值」
#2.「鍵」不存在，也沒有設定「預設值」，會傳回「None」。
#3.「鍵」不存在，但有設定「預設值」，會傳回預設值。



