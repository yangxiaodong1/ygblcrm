# Author : July  Yang 


def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = int(count / step)
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group # 扫描数据
                key = lists[j]# 当前数据
                while k >= 0 and lists[k] > key:
                    lists[k + group] = lists[k]
                    k -= group
                lists[k + group] = key
                j += group
        group = int(group/step)
    return lists

'''
 希尔算法: 搞懂希尔排序之前要搞懂直接插入排序
  不断的缩小增量，
  把下标按照一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，
  每一组包含的关键词也会越来越多的，，当增量减少到1的时候，整个文件切好被分成一组，算法终止
 
'''
def shell_sort2(arr):
    count = len(arr)
    group = int(count / 2)

    while group> 0: # 增量减少到1的时候
        for i in range(0,group): # 循环到增量间距的元素
            j =i+group # 下标为i,j 之间的元素是同意数组的元素
            while j<count:
                # 同一组的元素进行直接插入排序
                k =j-group #往后扫描的元素
                key = arr[j] # 要进行比较的元素
                while k>=0 and key<arr[k]:
                    arr[k+group] = arr[k]
                    k-=group
                arr[k+group]=key
                j+=group #不断循环上同一数组中的元素
        # 增量改变,将一个增量循环完的时候就要进行下一个增量
        group=int(group / 2)
    return arr




if __name__ == '__main__':
    arr = [90,2,10,89,30]
    print(shell_sort2(arr))







