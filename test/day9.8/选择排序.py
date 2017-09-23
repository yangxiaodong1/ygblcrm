
'''选择最小不动
'''

def slecte_sort(arr):
    count = len(arr)
    for i in range(0,count):
        min = i
        for j in range(i+1,count):
            if arr[min]>arr[j]:
                min = j
        arr[min],arr[i] = arr[i],arr[min]
    return arr

if __name__=="__main__":
    arr = [2222,33,656]
    print(slecte_sort(arr))
