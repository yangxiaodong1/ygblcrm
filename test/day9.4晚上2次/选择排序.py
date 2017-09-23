
def select_sort(arr):

    count = len(arr)

    for i in range(0,count):
        min = i
        j=i+1
        while j<count and arr[min]>arr[j]:
            min =j
            j+=1
        arr[min],arr[i] = arr[i],arr[min]

    return arr
if __name__=="__main__":
    arr = [1,99,89]
    print(select_sort(arr))