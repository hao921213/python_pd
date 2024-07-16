import numpy as np
#Numpy Array
a=np.array([1,2,3,4])
print(a)
b=np.array([(2.5,3),(3,4)],dtype=float)
print(b)
print(np.array([3,4,5]))
print(np.zeros(3))
print(np.ones(3))
print(np.arange(10))
print(np.arange(2,10,2))#np.arange(初始值,終值(不包含),間隔)
print(np.eye(3))#建立一個n*n的單位矩陣
print(np.random.random((2,3)))
print(np.linspace(0,10,4))#建立一個初值到終值均分成m份的矩陣

#I/O
array=np.array([1,2,3])
# np.save("my_array",array)
# np.savetxt("my_array.txt",array) 儲存陣列到檔案中

# array_from_data=np.load("my_array")
# print(array_from_data)
# array_from_data_txt=np.loadtxt("my_array.txt")
# print(array_from_data_txt) 讀檔案資料

#Data Types
print(np.array([1.2, 3, 5.2], dtype='i'))
print(np.array([1.2, 3, 5.2], dtype="int32"))
print(np.array([1.2,3,5.2],dtype='f'))
print(np.float32(1))

#Inspecting Your Array
a = np.array([1, 2, 3])
b=np.array([(1.3,2,4.5),(2,3,4)])
print(a.shape,b.shape)
print(len(a),len(b))
print(a.ndim,b.ndim)
print(a.size,b.size)
print(a.dtype,b.dtype)
print(a.dtype.name,b.dtype.name)

#Array Mathematics
a=np.array([1,2,3])
b=np.array([3,4,5])
c=np.array([1,4,9])
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))
print(np.sqrt(c))
print(np.sin(c))
print(np.cos(c))
print(np.log(c))

#Comparison
a,b=np.array([(1,2,3),(3,4,5)])
c=np.array([(2,2,4),(3,6,5)])
print(a==b)
print(a==c)
print(np.array_equal(a,b))

#Aggregate Functions
a,b=np.array([(1,2,3),(3,4,5)])
c=np.array([(2,2,4),(3,6,5)])
print(a==b)
print(a==c)
print(np.array_equal(a,b))
a = np.array([2, 5, 7])
b = np.array([(0, 1), (2, 3)])
print(a.sum)
print(a.min)
print(a.max)
print(a.max(axis=0))
print(np.median(a))
print(np.mean(a))
print(np.std(a))

#Copying & Sorting Arrays
a=[1,4,2,8,3,1,7]
print(a.sort())
b.copy(a)
print(b)





