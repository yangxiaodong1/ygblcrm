

def merger(left,right):
    i,j =0,0
    result =[]
    while i <len(left) and j <len(right):
        if left[i]<right[i]:
            result.append(left[i])
            i+=1
        elif left[i]> right[j]:
            result.append(right[j])
            j+=1

    result+=left[i:]
    result += right[j:]
    return result

def merger_sort(arr):

    #递归结束条件，递归的是分
    if len(arr)<=1:
        return arr
    num = int(len(arr) / 2)
    left = merger_sort(arr[:num])
    right =merger_sort(arr[num:])
    return merger(left,right)

if __name__=="__main__":
    arr = [2,200,3]
    print(merger_sort(arr))