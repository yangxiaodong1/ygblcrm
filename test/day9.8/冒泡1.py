
def maopao(arr):
    count = len(arr)
    for i in range(0,count):
        for j in range(i+1,count):
            if arr[j]<arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
if __name__=="__main__":
    arr = [2222,33,656]
    print(maopao(arr))