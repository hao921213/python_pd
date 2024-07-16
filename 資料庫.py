import sqlite3
cn=sqlite3.connect("myDb.db")
try:
    sqlstr="CREATE TABLE 產品(編號 text,品名 text,單價 int)"
    cn.execute(sqlstr)
    cn.commit()
    print("產品已更新完成")
except Exception:
    print("產品已存在，無法更新")
cn.close()