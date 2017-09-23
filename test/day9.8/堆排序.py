

def adjust_heap(arr,i,size):
    lchild = i*2+1
    rchild = i*2 +2
    max =i
    if i<int(len(arr) / 2):
        if lchild<size and arr[max]<arr[lchild]:
            max = lchild
        if rchild<size and arr[max]<arr[rchild]:
            max = rchild
        if max !=i:
            arr[max],arr[i] = arr[i],arr[max]
def build_heap(arr,size):
    for i in range(0,int(size/2))[::-1]:
        adjust_heap(arr,i,size)

def heap_sort(arr):
    size =len(arr)
    build_heap(arr,size)
    for i in range(0,size)[::-1]:
        arr[0],arr[i] = arr[i],arr[0]
        build_heap(arr,i)
    return arr

if __name__=="__main__":
    arr = [2222,33,656]
    print(heap_sort(arr))
