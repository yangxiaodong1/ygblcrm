
def quick_sort(arr,left,right):
    #一定要有出口
    if left>=right:
        return arr
    low = left
    high = right
    key =arr[left]

    while left<right:

        while left<right and key<arr[right]:
            right-=1
        while left<right and key >arr[left]:
            left +=1
        arr[left],arr[right] = arr[right],arr[left]

    arr[left] = key
    quick_sort(arr,low,left-1)
    quick_sort(arr,left+1,high)
    return arr

if __name__=="__main__":
    arr =[9,30,22]
    print(quick_sort(arr,0,len(arr)-1))