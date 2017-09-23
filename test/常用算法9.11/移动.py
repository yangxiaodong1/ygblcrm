# Author : July  Yang 
#ab**cd**e*12 处理后*****abcde12
import re


def count_move(arr):
    al = arr.replace('*','')
    notal = re.sub('[^*]','',arr)
    count = arr.count('*')
    print(notal,'===',count)



arr = "ab**cd**e*12"

count_move(arr)




