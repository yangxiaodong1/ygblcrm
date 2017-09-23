
''' 当前元素，扫描元素'''

def insert_sort(arr):
    count = len(arr)
    for i in range(1,count):
        j=i-1
        key = arr[i]
        while j>=0 and key <arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

if __name__=='__main__':
    arr = [2,44,56,9]
    print(insert_sort(arr))
