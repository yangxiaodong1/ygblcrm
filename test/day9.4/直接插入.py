# Author : July  Yang 

# 直接插入排序，
'''
  通过构建有序序列，对于未排序的数据，在已经排序序列中从后向前扫描，找到相应位置并插入
  插入排序的核心：假设第一个元素排好，之后的元素对排好的部分从后向前比较并且逐渐移动
'''

def insert_sort(arr):
    count = len(arr)

    for i in range(1,count):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key
    return arr



def insert_sort(arr):
    count = len(arr)
    for i in range(1,arr):
        key =arr[i]
        j = i-1
        while  j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

'''
    理解：
    1，取第一个元素，默认已经排好序的
    2.去下一个元素，把已经排好序的从后向前扫描，
    3扫描到的这个元素和新元素比较如果扫描到的元素比新元素大则往后移动一位
    4 重复3的步骤，知道扫描的元素小于等于新元素就把新元素插入到扫描位置的前一位
    
    可以说就是 （比较移动插入）
'''
def insert_sort3(arr):
    count = len(arr)
    for i in range(1,range): # 取第一个元素，默认是排好序的
        key = arr[i] # 取这个新元素
        j=i-1 # 向后扫描
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j] # 当扫描的元素大于新的元素就扫描的元素向后移动一位继续扫描
            # 继续扫描
            j-=1 #
        arr[j+1] = key # 将这个新元素插入法到扫描到元素的后一位

    return arr # 返回这个排序好的数组


def insert_sort4(arr):
    count = len(arr)
    for i in range(1,count):
        key =arr[i]
        j=i-1
        while j>=0 and key< arr[j]:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] =key
    return arr



if __name__ == "__main__":
    arr = [1,10,2,8,3]
    print(insert_sort(arr))






