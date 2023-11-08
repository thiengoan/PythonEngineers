import numpy as np 

# l = list(range(1,4))
# print(l)
# data = np.array(l)
# print(data)

l = [1,2,3,4,5,6]
data = np.array(l)
tong = 0
tich = 1
for i in data:
    tong += i
    tich *= i
print(tong,tich)

l = [[1,2,3],[4,5,6]]
data = np.array(l)
tong = 0
tich = 1
for i in data:
    for j in i:
        tong += j
        tich *= j
        print(i,j)
print(tong,tich)