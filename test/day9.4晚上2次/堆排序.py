
def adjust_heap(arr,i,size):
    lchild = 2*i + 1
    rchild = 2*i + 2
    max = i

    if i < (size / 2):
        if lchild <size and arr[max]<arr[lchild]:
            max = lchild
        if rchild <size and arr[max] < arr[rchild]:
            max = rchild
        if max !=i:
            arr[max],arr[i] = arr[i],arr[max]


# 创建初始化堆
def build_heap(arr,size):
    for  i in range(0,int(size /2))[::-1]:
        adjust_heap(arr,i,size)

def head_heap(arr):
    size = len(arr)
    build_heap(arr,size)
    for i in range(0,size)[::-1]:
        arr[0],arr[i] = arr[i],arr[0]
        build_heap(arr,i)
    return arr


###############################################################
def adjust_heap2(arr,i,size):
    rchild =2*i + 1
    lchild = 2*i + 2
    max = i
    if i < int(size / 2):
        if lchild <size and arr[max]<arr[lchild]:
            max = lchild
        if rchild <size and arr[max] < arr[rchild]:
            max = rchild
        if max != i:
            arr[max],arr[i] = arr[i],arr[max]

def build_heap2(arr,size):

    for i in range(0,int(size / 2))[::-1]:
        adjust_heap2(arr,i,size)
def heap_sort2(arr):
    size = len(arr)
    build_heap2(arr,size)
    for i in range(0,size)[::-1]:
        arr[0],arr[i] = arr[i],arr[0]
        build_heap2(arr,i)
    return arr


if __name__=="__main__":
    arr = [32,5,324]
    print(heap_sort2(arr))