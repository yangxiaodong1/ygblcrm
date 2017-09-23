
'''当前元素和扫描'''

def insert(arr):
    count =len(arr)
    for i in range(1,count):
        j = i-1
        key =arr[i]
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

if __name__=="__main__":
    arr = [2222,33,656]
    print(insert(arr))