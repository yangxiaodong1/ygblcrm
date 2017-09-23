

def insert_sort(arr):
    count=len(arr)

    for i in range(0,count):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

if __name__=='__main__':
    arr=[2,42,3]
    print(insert_sort(arr))