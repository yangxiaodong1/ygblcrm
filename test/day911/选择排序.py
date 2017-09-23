


def select_sort(arr):
    count = len(arr)
    for i in range(0,count):
        min = i
        for j in range(i+1,count):
            if arr[j]<arr[min]:
                min = j
        arr[min],arr[i] =arr[i],arr[min]
    return arr