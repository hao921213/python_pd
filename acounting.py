import tkinter as tk
import sqlite3 as sql3
import time

t=time.time()
tt=time.localtime(t)
year=tt.tm_year
month=tt.tm_mon
day=tt.tm_mday
date="{0}/{1}/{2}".format(tt.tm_year,tt.tm_mon,tt.tm_mday)

cn=sql3.connect("Acount.db")
print("Database has been connected")
try:
    sqlstr="CREATE TABLE 記帳(消費類別 text,消費品名 text,消費金額 int,消費日期 text)"
    cn.execute(sqlstr)
    print("database has been created")
    cn.commit()
except Exception:
    print("產品已存在")



mytk=tk.Tk()
mytk.title("記帳小本本")
mytk.geometry("400x600")
mytk.configure(bg='#ECFFFF')

#日期
date_tk=tk.Label(mytk,text="Date:"+date,font=('Arial',10),padx=0,pady=0,bg="#ECFFFF")
date_tk.grid(row=0,column=0)
#消費類別
category=tk.Listbox(mytk,width=15,height=10)
category.insert(1,"food")
category.insert(2,"daily")
category.insert(4,"entertainment")
category.insert(5,"learning")
category.insert(6,"transportation")
category.grid(row=1,column=0)

mytk.mainloop()

cn.close()