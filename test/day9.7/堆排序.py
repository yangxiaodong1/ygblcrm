
'''初始化，交换'''

def adjust_heap(arr,i,size):
    lchild = 2*i +1
    rchild = 2*i +2
    max = i
    if i <int(size / 2):
        if lchild <size and arr[max] <arr[lchild]:
            max = lchild
        if rchild <size and arr[max] <arr[rchild]:
            max = rchild
        if max !=i:
            arr[max],arr[i] = arr[i],arr[max]
def buid_heap(arr,size):
    for i in range(0,int(size / 2))[::-1]:
        adjust_heap(arr,i,size)
def heap_sort(arr):
    size =len(arr)
    buid_heap(arr,size)
    for i in range(0,size)[::-1]:
        arr[0],arr[i] = arr[i],arr[0]
        buid_heap(arr,i)

    return arr

if __name__=='__main__':
    arr = [2,44,56,9]
    print(heap_sort(arr))