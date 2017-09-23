# Author : July  Yang 
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < int(size / 2):
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]

def build_heap(lists, size):
    for i in range(0, int((size/2)))[::-1]:
        adjust_heap(lists, i, size)
def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        #adjust_heap(lists, 0, i)
        build_heap(lists,i)
    return lists
if __name__ == "__main__":
    arr = [90,3,20,30,2]
    print(heap_sort(arr))






