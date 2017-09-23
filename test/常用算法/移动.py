# Author : July  Yang 
#ab**cd**e*12 处理后*****abcde12
import re

def sort(arr):

    char_new = arr.replace("*","")
    lists = list(arr)
    count = lists.count("*")
    result = []
    for i in range(0,len(lists)):
        if lists[i] == "*":
            result.append(lists[i])
    result+=char_new
    arr = ''.join(result)
    print(arr,"--------------",count)





# char_new2 = arr.replace([^*],'k')


def count_move(old_string):
    char_new = old_string.replace("*","")
    char_new2 = re.sub("[^*]", '', old_string)
    count = old_string.count("*")
    print(char_new2+char_new,"---------count----",count)

arr = "ab**cd**e*12"

count_move(arr)




