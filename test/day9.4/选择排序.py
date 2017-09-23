# Author : July  Yang 

'''
    每趟从待选排序的记录里面选出关键字最小的记录，
    顺序放在已经排序的记录序列末尾，直到全部排序结束为止
'''

def select_sort(lists):
    count = len(lists)
    for i in range(0,count):
        min =i
        for j in range(i+1,count):
            #两个相邻2的比较 ,经过内循环之后 就找到最小值的下标了
            if lists[min]>lists[j]:
                min = j
        # 交换 循环的这个位置和最小值，最小值放在开始循环的位置
        lists[i],lists[min]=lists[min],lists[i]


    return lists


def select_sort2(arr):
    count = len(arr)
    for i in range(0,count):
        min = i
        for j in range(i+1,count):
            if arr[min]>arr[j]:
                min = j
        arr[min],arr[i] = arr[i],arr[min]
    return arr






if __name__ == '__main__':
    arr = [1, 9, 2, 5, 4]
    arr2= [1, 9, 2, 5, 4]
    print(select_sort(arr2))






