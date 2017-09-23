
def inset_sort(arr):
    '''倒序扫描'''

    count = len(arr)
    for i in range(1,count):
        key = arr[i]
        j = i -1

        while j>=0 and key <arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

    return  arr
if __name__=="__main__":
    arr = [3,444,4656456,99]
    print(inset_sort(arr))