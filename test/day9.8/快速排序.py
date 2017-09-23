
def quick_sort(arr,left,right):
    low =left
    high = right
    key = arr[left]
    while left <right:
        while left<right and key<arr[right]:
            right-=1
        while left<right and key >arr[left]:
            left+=1
        arr[left],arr[right] = arr[right],arr[left]
    quick_sort(arr,low,left-1)
    quick_sort(arr,left+1,hig)