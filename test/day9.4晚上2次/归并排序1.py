def merger(arr,left,right):
    i,j=0,0
    result = []
    while left<right:

        if left <right and left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result +=left[i:]
    result +=right[j:]
    return result

def merger_sort(arr):
    if len(arr)<=1:
        return arr
    num =int(arr / 2)
    left = merger_sort(arr[:num])
    right = merger_sort(arr[num:])
    return merger(arr,left,right)

