a = int(input('nhap so a:'))
b = int(input('nhap so b:'))
# no1 In số chẳn từ a->b
for i in range(a,b + 1):
    if i % 2 == 0:
        print(i)

# no2 In số nguyên tố từ a->b
def snt(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(a,b + 1):
    if snt(i):
        print(i)

# no3 Kiem tra so nguyen to
c = int(input('nhap so c:'))

if snt(c):
    print('{} là số nguyên tố'.format(c))
else:
    print('{} ko là số nguyên tố'.format(c))

# no4 Thêm phần tử vào list
mylist = [1,2,3,4]
def addList(a):
    mylist.append(a)
    return [i for i in mylist]

d = input('nhập phần tử muốn thêm vào list: ')
print(addList(d))

#no5 Xoa key trong dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

def delItem(key):
    if key in thisdict:
        thisdict.pop(key)
    else:
        print('key ko ton tai')
    return thisdict

key = input('nhap key muon xoa:')
print(delItem(key))

#no6 Tạo dict từ 2 list
list1 = [1,2,3]
list2 = [3,4,5]

def createDic(list1,list2):
    return dict(zip(list1, list2))

print(createDic(list1, list2))

#no7 Tìm value lớn nhất trong dict
dic = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

ls = list(zip(dic.values(), dic.keys()))
print(max(ls)[0])

# No8 Đếm phần tử giống nhau trong mảng
ls = [1,2,4,6,2,4,5,2,4,5,6,2,4,4]

def countItem(list,item):
    print(list.count(item))

a = int(input('Nhập phân từ cần đếm: '))
countItem(ls,a)