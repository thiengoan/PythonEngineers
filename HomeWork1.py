'''
Name: TRAN THIEN NGOAN 
Class: MSE14

HOMEWORK 1

1. Viết 1 hàm để tìm key có giá trị lớn nhất trong 1 dictionary
2. Viết 1 hàm để đếm số lần xuất hiện của 1 phần tử trong list
3. Kiểm tra định dạng mật khẩu mạnh. Yêu cầu: Viết một chương trình Python để kiểm
tra xem một chuỗi định dạng mật khẩu có mạnh hay không. Mật khẩu mạnh cần có ít
nhất 8 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt.
4. Tách tên họ từ một danh sách người dùng. Yêu cầu: Viết một chương trình Python
để tách tên và họ từ một danh sách người dùng có định dạng &quot;Họ và tên&quot; bằng sử
dụng regular expressions.

'''
################################################################
# 1 Viết 1 hàm để tìm key có giá trị lớn nhất trong 1 dictionary

def get_max_value(dictionary):
    max_value = 0 
    key_value = ''
    for key in dictionary:
        if dictionary[key] > max_value:
            max_value = dictionary[key]
            key_value = key
    return (key_value,max_value)
        
#input:        
dictionary = {
    'a': 10,
    'b': 50,
    'c': 100,
    'd': 400
}
print(dictionary)
print(get_max_value(dictionary))
#output: ('d', 400)

################################################################
# 2. Viết 1 hàm để đếm số lần xuất hiện của 1 phần tử trong list

def countItem(list,item):
    return list.count(item)
# input:
list = [1,2,4,6,2,4,5,2,4,5,6,2,4,4]
print(list)
input = int(input('Nhập phần tử cần đếm trong list: '))

#output:
print(countItem(list,input))

####################################################################################
# 3. Kiểm tra định dạng mật khẩu mạnh. Yêu cầu: Viết một chương trình Python để kiểm
# tra xem một chuỗi định dạng mật khẩu có mạnh hay không. Mật khẩu mạnh cần có ít
# nhất 8 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt.

import re

def check_password(password):
    if len(password) < 8:
        print('Mật khẩu phải từ 8 ký tự trở lên.')
        return False
    if not re.search("[A-Z]", password):
        print('Mật khẩu phải có chứa ký tự chữ hoa A-Z')
        return False
    if not re.search("[a-z]", password):
        print('Mật khẩu phải có chứa ký tự chữ thường a-z')
        return False
    if not re.search("[0-9]", password):
        print('Mật khẩu phải có chứa số 0-9')
        return False
    if not re.search("[!@#$%^&*()_+-={}|\\:;\"'<>,.?/]", password):
        print('Mật khẩu phải có chứa các ký tự đặc biệt')
        return False
    print('Mật khẩu đã đủ mạnh')
    return True

#input: 
pass1 = '12345678'
pass2 = '22nAABG##@'

#output:
print(check_password(pass1))
print(check_password(pass2))

#######################################################################
# 4.Tách tên họ từ một danh sách người dùng. Yêu cầu: Viết một chương trình Python
# để tách tên và họ từ một danh sách người dùng có định dạng "Họ và tên" bằng sử
# dụng regular expressions.

import re
def split_name(list):
    list1 = [] # Danh sách Họ
    list2 = [] # Danh sách Tên
    for name in list:
        pattern = '\S+' 
        full_name = re.findall(pattern,name)
        first_name = full_name[0]
        full_name.pop(0)
        last_name = ' '.join(full_name)
        list1.append(first_name)
        list2.append(last_name)
    return list1,list2

#input:       
list = ['Tran Thien Ngoan', 'Nguyen Van An', 'Hoang Chien', 'Nguyen Hoang Gia Huy']
print(list)

#output:
print(split_name(list))