
def adjust_heap(list,i,size):
    ichildren = 2*i + 1
    rchildren = 2*i + 2
    max = i # 临时max有大用
    if i< int(size/ 2):
        if ichildren<size and list[max]< list[ichildren]:
            max = ichildren
        if rchildren<size and list[max]<list[rchildren]:
            max = rchildren
        if max !=i:
            # 不相等的时候要交换，如果相等就不需要交换
            list[max],list[i] =list[i],list[max]

# 创建和初始化堆
def build_heap(list,size):
    for i in range(0,int(size / 2))[::-1]:
        adjust_heap(list,i,size)

def heap_sort(lists):
    size =len(lists)
    build_heap(lists,size)
    for i in range(0,size)[::-1]:
        lists[0],lists[i] =lists[i],lists[0]
        build_heap(lists,i)
    return lists

if __name__=="__main__":
    arr = [2,33,45,21]
    print(heap_sort(arr))