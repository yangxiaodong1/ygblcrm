
'''基准数的左边右边'''

def quick_sort(arr,left,right):
    if left >=right:
        return arr
    low = left
    high = right
    key =arr[left]

    while left<right:
        while left<right and key<arr[right]:
            right-=1
        while left<right and key>arr[left]:
            left+=1
        arr[right],arr[left] = arr[left],arr[right]
    arr[left] = key
    quick_sort(arr,low,left-1)
    quick_sort(arr,left+1,high)
    return arr

if __name__=='__main__':
    arr = [23,2,4456]
    print(quick_sort(arr,0,len(arr) -1))
