
'''最小下标'''

def select_sort(arr):
    count = len(arr)
    for i in range(0,count):
        min = i
        for j in range(i+1,count):
            if arr[j] <arr[min]:
                min = j
        arr[min],arr[i] = arr[i],arr[min]
    return arr
if __name__=='__main__':
    arr = [2,44,56,9]
    print(select_sort(arr))