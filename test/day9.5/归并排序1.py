
'''分治方法，先分后合并'''

def merge(left,right):
    i,j=0,0
    result = []
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result += left[i:]
    result += right[j:]
    return result

def merger_sort(arr):

    if len(arr)<=1:
        return arr
    num = int(len(arr) / 2)

    left = merger_sort(arr[:num])
    right = merger_sort(arr[num:])
    return merge(left,right)

if __name__=="__main__":
    arr = [3,89,489,99]
    print(merger_sort(arr))