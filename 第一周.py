#Lab 1-1
print("Hello Python")


#print(values[%(參數串列)][,sep=間格符號][,end=結尾字串])
print("多吃水果")
print(100,"多吃水果",60)#sep的預設為空格，故文字間會有空格,end的預設值為換行
print(100,"多吃水果",60,sep="&")
print(100,60,sep="&",end="")#end為空格，故下一個輸出不會跳到下一行，會輸出在同一行
print("結尾")


#基本資料型態
print("百分比%s%%"%("九十九"))#%s會找%()中的第一個string，%%為輸出%
print("%s%d瓶,共%f元"%("可樂",9,9*16.25))#%d則會找integer並用十進位輸出，%f則是找float
print("%d的八進制為%o"%(10,10))#%o會找integer並用八進位輸出
print("%c"%("A"))#%c則是找後面的char輸出若是integer則輸出該數字對應到ASCII碼上的char
print("%c"%(65))


#設定寬度來格式化輸出資料
print("%d"%(1234))
print("%6d"%(1234))#d前面的數字是設定總共輸出幾格，一開始數字預設靠右
print("%06d"%(1234))#0則代表多餘的格數補零
print("%3d"%(-1234))#若格數不足則全部顯示
print("%4.2s"%("ABC"))#設定格數為四並取字串中前兩個字   只有字串有這個用法


#格式化浮點數輸出
print("%f"%(123.45))#若沒有設定格數，小數位預設為六格多餘補零，注意小數點.會佔格數
print("%f"%(-123.45))#負數符號也佔一格
print("%.2f"%(-123.456))#小數點後二代表四捨五入到第二位
print("%8.2f"%(-123.456))#格數為8然後四捨五入到第二位與字串的用法不同
print("%E"%(1234567.8))#表示成科學記號，小數位預設一樣是六格多餘補零
print("%e"%(1234567.8))
print("%10.2e"%(1234567.8))#要注意e跟+-會佔掉格數


#修飾字元
print("%#x"%(1234))# #x代表0x+後面數值轉成16進制，#b代表0b+後面數值轉成2進制，0o+後面數值轉成8進制
print("%#o"%(1234))
print("%06d"%(1234))#多餘格數補零
print("%-6d"%(1234))#-代表向左靠齊
print("% d"%(1234))#空格位置代表輸出時那一格空格


#逸出順序
print("1234\a")#\a代表發出警告音
print("1234\b56")#\b代表游標向左一個然後繼續輸出
print("12345\n",end="")#\n換行 常用
print("123\r456")#\r回到字首繼續輸出
print("1234\t456")#\t插入五個空格
print("\\,\',\"")#輸出\,',"

