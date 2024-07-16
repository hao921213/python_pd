import time

t=time.time()
tt=time.localtime(t)
print(time.localtime(t))
print(tt.tm_year)
print(tt.tm_mon)
print(tt.tm_mday)