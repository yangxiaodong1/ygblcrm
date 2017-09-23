'''


初始化堆，交换，再初始化堆
'''

def adjust_heap(arr,i,size):
    lchild = 2*i + 1
    rchild = 2*i +2

    if i< int(size / 2): # 不是要循环下去的
        max =i
        if lchild<size and arr[max]<arr[lchild]:
            max = lchild
        if rchild<size and arr[max]<arr[rchild]:
            max =rchild
        if max !=i:
            arr[max],arr[i] = arr[i],arr[max]

def build_heap(arr,size):
    for i in range(0,int(size / 2))[::-1]:
        adjust_heap(arr,i,size)

def head_sort(arr):
    size =len(arr)
    build_heap(arr,size)
    for i in range(0,size)[::-1]:
        arr[0],arr[i] =arr[i],arr[0]
        build_heap(arr,i)
    return arr
if __name__=="__main__":
    arr = [456,5,77]
    print(head_sort(arr))