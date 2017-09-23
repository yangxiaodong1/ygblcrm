
'''扫描，当前元素'''

def insert_sort(arr):
    count = len(arr)
    for i in range(1,count):
        j=i-1 # 扫描元素
        key = arr[i] # 比较元素
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key

    return arr
if __name__=="__main__":
    arr = [12,33,4]
    print(insert_sort(arr))
