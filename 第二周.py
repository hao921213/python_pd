#format(資料,格式字串)
print(format(100,'4d'))# 4:寬度,d:型態字元(整數)
print(format(25,'o'))#o:型態字元(十六進制)
print(format(12.345,'<8.1f'))#<:靠左對齊
print(format(0.845,'8.2%'))#%以百分比呈現結果
print(format('Python','^10s'))#^:靠中間


#變數=input([提示字串])
print(int(input("請輸入現在幾月:")))
#eval(字串)可以將整數或浮點數字串，自動轉型成對應的資料型態
print(eval('2*4'))
print(type(eval('2*4')))
print(eval('123'),eval('12.34'))
eval('print(2+3)')
print(eval("2+3"))
print(int('123')+int("34"))
print(eval("123+34"))
print(float('12.34'))
print(float('123'))
print(int(12.34))
print(int("12.34"))#無法輸出


#Lab 1-3
stu_name=input("請輸入姓名:")
stu_num=int(input("請輸入座號:"))
stu_sco=float(input("請輸入分數:"))
print("姓名:%s\t座號:%d\t分數:%2.3f"%(stu_name,stu_num,stu_sco))


#變數
a=b=c=20
print(a,b,c)
age,name=18,'Eason'
print(age,name)


#del 變數名稱(將變數刪除，節省記憶體)
score=10
del score


#整數資料型態
#type():取得資料型態,bin():十轉二,oct():十轉八,hex():十轉十六,int():其他進制或字串轉整十
num=21
print(type(num),bin(num),oct(num),hex(num),int('21')+3)


#布林資料型態(只有空值及0會回傳False)
b=False
print(type(b))
print(bool(1))
print(bool(0))#只有0或空才會輸出False，其餘則是True
print(bool())
print(bool(-1),bool('程式'))


#浮點數資料型態
#float.is_integer(浮點數)
f,i=1.2345,12345
print(type(f))
f2=float(i)
print(f2)#float(整數)在小數位後會多一個0
f3=float('123.45')
print(float.is_integer(f3))#檢查此float是否為整數，即小數位後為0
print(float.is_integer(f2))
#round(浮點數,位數)預設值為四捨五入到整數位
print(round(f,2))
print(round(f))


#Lab 02-A
username="張無忌"
pointers=1357.85
power=98
print("username值為",username,"型態為",type(username))
print("pointers值為",pointers,"型態為",type(pointers))
print("power值為",power,"八進制值為",oct(power))
print(username+"生命值為",power,"點數為",round(pointers,1))


#算術運算子
print(12+3,12-3,12*3,12/3,12%3,12//3,12**3)
#Lab 3-1
w,h=150,66
h=h**2
print('BMI=',w/h*703)

#關係運算子
#==
print(2+3==1+4,2+3==4)
#!=
print(2+3!=1+4,2+3!=4)
#> or < or >= or <=
print(2+1>2,2+1>4)


#邏輯運算子
#not and or
print(not(3>5),not(5>3))
print((5>3) and (9>6),(5<3) and (9>6),(5>3) and (9<6),(5<3) and (9<6))
print((5>3) or (9>6),(5<3) or (9>6),(5>3) or (9<6),(5<3) or (9<6))


#複合指定運算子
i=0
i+=3 #i=i+3
i-=3 #i=i-3
i*=3
i/=3
i%=3
i//=3


#Lab 3-2
nat=int(input("請輸入自然成績:"))
mat=int(input("請輸入數學成績:"))
eng=int(input("請輸入英文成績:"))
sum=nat+mat+eng
aver=(sum)/3
print("總分:%d 平均:%f"%(sum,aver))


#位元運算子
A,B=True,True
print(A&B,A|B,A^B,~A,~B)#&為and,|為or,^為Xor,~為not     問~A
A,B=True,False
print(A&B,A|B,A^B,~A,~B)
A,B=False,True
print(A&B,A|B,A^B,~A,~B)
A,B=False,False
print(A&B,A|B,A^B,~A,~B)


#移位運算子
print(20>>1,20<<1)#>>往右一個位元有除2的作用，<<往左一個位元有乘2的作用


#Lab 3-3
x=8
print("立方體的邊長:",x)
print("立方體的表面積:",x*x*6)
print("立方體的體積:",x*x*x)

#自動型態轉換
b,i,f=True,2,6.6
print(b+i,b+f,i+f)#b+i時b自動轉成1,b+f時b自動轉成1.0,i+f時i自動轉成2.0
print(b-i,b-f,i-f)
print(b*i,b*f,i*f)
print(b/i,b/f,i/f)


#強制型態轉型
#整數轉浮點->float(整數資料)
#浮點轉整數->int(浮點數資料)
#浮點轉整數->round(浮點數資料)
#數值轉字串->str(數值資料)
#轉布林->bool(資料)
#大轉小容易失真


#Lab 3-A
money=int(input("請輸入總貸款金額:"))
year=int(input("請輸入幾年還清:"))
month=float(year*12)
rate_year=int(input("請輸入年利率:"))
rate_month=float(rate_year/12/100)
ans=float((((1+rate_month)**month)*rate_month)/(((1+rate_month)**month)-1))
print(round(money*ans,1))


#Lab 4-2
x=45
y=int(input("請輸入購買金額:"))
if x-y<0:
    print("餘額不足\n","自動加值")
    x+=500
x-=y
print("餘額:",x)


#Assingment 1-1
x=int(input("請輸入月份:"))
if x==12 or x==1 or x==2:
    print("現在是冬天，請隨時加件厚外套。")

