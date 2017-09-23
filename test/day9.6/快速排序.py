
'''基准数，左右交换，先遍历，满足停下来'''

def quick_sort(arr,left,right):
    if left >=right:
        return arr
    low =left
    high = right
    key =arr[left]

    while left <right:
        while left<right and key<arr[right]:
            right -=1
        while left<right and key > arr[left]:
            left +=1
        arr[left],arr[right] = arr[right],arr[left]

    arr[left] = key
    quick_sort(arr,low,left-1)
    quick_sort(arr,left+1,high)
    return arr

if __name__ == "__main__":
    arr = [388,99,3]
    print(quick_sort(arr,0,len(arr)-1))
