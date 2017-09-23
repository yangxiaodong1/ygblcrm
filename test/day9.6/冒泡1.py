
def maopao(arr):
    count = len(arr)
    for i in range(0,count):
        for j in range(i+1,count):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr

if __name__=="__main__":

    arr = [3,5,34,1]
    print(maopao(arr))

