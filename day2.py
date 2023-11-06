''' 
ReGex in Python

1. Match
2. Search
3. Findall
4. Split
5. Sub

'''

import re
# string = 'hello 12 hi 89. Howdy 34'
# pattern = '\d+'
# result = re.findall(pattern,string)
# result = list(map(int,result)) # convert str to int
# print(result)

# Tim cac dia chi email trong chuoi

# string = 'my email address are thiengoan@gmail.com test test@gmail.com.'
# pattern = '\S+@\S+[^\s\.]'
# result = re.findall(pattern,string)
# print(result)

# list = ["apple", "banana", "cherry", "avocado", "blueberry"]
# for i in list:
#     if re.match('^[ab]',i):
#         print(i)


# log_file = open('error_log.txt', 'r')
# log_text = log_file.read()
# log_file.close()
# pattern = '.*[eE]rror.*'
# result = re.findall(pattern,log_text)
# print(result)

# no1
# def findNumber(text):
#     pattern = '\d+'
#     result = re.findall(pattern,text)
#     if result:
#         print('co so nguyen')
#     else:
#         print('Ko co so nguyen')
#     return result

# text = '55nhap text: dsdsdsdsdsd 7'
# findNumber(text)


# no3
# def validEmail(email):
#     pattern = r'[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]'
#     if re.match(pattern,email):
#         print('email hop le')
#         return True
#     else: 
#         print('khong hop le')
#         return False

# email = 'thiengoan@gmail.com'
# validEmail(email)

#no6
# log_file = open('error_log.txt', 'r')
# log_text = log_file.read()
# log_file.close()
# pattern = r'\(?[0-9]{3}\)?+\-[0-9]{3}+\-[0-9]{4}'
# result = re.findall(pattern,log_text)
# print(result)
import re

def split_name(list):
    list1 = []
    list2 = []
    for name in list:
        pattern = '\S+' 
        full_name = re.findall(pattern,name)
        first_name = full_name[0]
        full_name.pop(0)
        last_name = ' '.join(full_name)
        list1.append(first_name)
        list2.append(last_name)
    return list1,list2
       
list = ['Tran Thien Ngoan', 'Nguyen Van An', 'Hoang Chien', 'Nguyen Hoang Gia Huy']
print(list)
print(split_name(list))