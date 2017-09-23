# Author : July  Yang 

# 排序
def merge(left,right):
    i,j=0,0
    result = []
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result +=left[i:]
    result +=right[j:]
    return result

def merger_sort(arr):
    # 出口
    if len(arr)<=1:
        return arr
    num = int(len(arr)/2)
    left =merger_sort(arr[:num]) #左边有序
    right =merger_sort(arr[num:])# 右边有序
    return merge(left,right)#  将两个有序序列合并，记住递归是有去有回 ，left,right 算是去，再归并回来



''''
 分治法：先递归分治后到出口了再归并到一起
 left right 不停的分，分好后再比较和合并到一起
'''

def merge2(left,right):
    #i j 是用作两个不同的数组的下标的
    #临时数组存长度的
    i,j=0,0
    result = []
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result +=left[i:]
    result +=right[j:]
    return result # 最后都要把排序好的给返回去

def merge_sort2(arr):
    if len(arr)<=1:
        return arr
    num = int(len(arr) / 2)
    left = merger_sort(arr[:num]) # 递归到左右单个
    right = merger_sort(arr[num:])
    return merge2(left,right) # 递归回来了归并






if __name__ == "__main__":
    arr=[90,80,89,20,72]
    print(merge_sort2(arr))






