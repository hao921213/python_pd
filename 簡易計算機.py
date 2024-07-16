import tkinter as tk

mytk=tk.Tk()
mytk.title("簡易兩個數字的計算機")
mytk.geometry("400x200")
num1=tk.IntVar()
num2=tk.IntVar()
num1_in=tk.Entry(mytk,width=10,textvariable=num1)
num2_in=tk.Entry(mytk,width=10,textvariable=num2)
tk.Label(mytk,text="num1:",padx=50,pady=30).grid(row=1,column=0)
tk.Label(mytk,text="num2:").grid(row=2,column=0)
num1_in.grid(row=1,column=1)
num2_in.grid(row=2,column=1)

def plus():
    v_num1=num1.get()
    v_num2=num2.get()
    num=v_num1+v_num2
    ans['text']='ans={0}'.format(num)
def minus():
    v_num1=num1.get()
    v_num2=num2.get()
    num=v_num1-v_num2
    ans['text']='ans={0}'.format(num)
def mutiply():
    v_num1=num1.get()
    v_num2=num2.get()
    num=v_num1*v_num2
    ans['text']='ans={0}'.format(num)
def division():
    v_num1=num1.get()
    v_num2=num2.get()
    num=v_num1/v_num2
    ans['text']='ans={0}'.format(num)

btn_plus=tk.Button(mytk,text="+",width=5,command=plus)
btn_minus=tk.Button(mytk,text="-",width=5,command=minus)
btn_mutiply=tk.Button(mytk,text="x",width=5,command=mutiply)
btn_division=tk.Button(mytk,text="/",width=5,command=division)

btn_plus.grid(row=3, column=0, padx=5, pady=5)
btn_minus.grid(row=3, column=1, padx=5, pady=5)
btn_mutiply.grid(row=3, column=2, padx=5, pady=5)
btn_division.grid(row=3, column=3, padx=5, pady=5)

ans=tk.Label(mytk,text="")
ans.grid(row=1,column=2)
mytk.mainloop()
