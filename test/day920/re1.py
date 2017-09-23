# Author : July  Yang 

import re

# pattern = re.compile(r'www\.(.*)\.(.*)')
# pattern = re.compile(r'www\.(.*)\.(.*)')
#
# m = pattern.match('www.baidu.com')
#
# print(m.group())
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))

# m2 = re.match(r'www\.(.*)\.(.*)','www.baidu.com')
# print(m2.group())
# print(m2.group(1))
# print(m2.group(2))
# m2 = re.search(r'www\.(.*)\.(.*)','www.baidu.com')
# print(m2.group())
# print(m2.group(1,2))
# print(m2.group(2))

# s="This is a number 234-235-22-423"
# r=re.match(".+(\d+-\d+-\d+-\d+)",s)
# print(r.group(1))
import re
# text = 'pythontab'
# m = re.match(r"\w+", text)
# if m:
#   print(m.group(0))
# else:
#   print('not match')
#
# m= re.match(r'\w+',text)
# if m:
#     print(m.group(0))
# p = re.compile(r'\d+')
# print(p.split('one1two2three3four4'))
# p = re.compile(r'\d+')
# print(p.findall('one1two2three3four4'))

# p = re.compile(r'\d+')
#
# for i in p.finditer('one1two2three3four4'):
#     print(i.group())

# import re
# text = "JGood is a handsome boy, he is cool, clever, and so on..."
# print(re.sub(r'\s+', '-', text,2))

# import re
# text="(021)88776543 010-55667890 02584533622 057184720483 837922740"
# m=re.findall(r"\(?0\d{2,3}[) -]?\d{7,8}",text)
# if m:
#     print(m)
# else:
#     print('not match')
import re


if re.match(r"^([0-9]{1,3}\.){3}[0-9]{1,3}$","272.168.1.1"):
    print("H奥")
else:
    print('BU')