# Author : July  Yang 

'''
 选择一个基准数， 大于这个基数的放在右边，小于这个基数的放在左边
 最后分成2部分 ，递归实现
'''

def quick_sort(arr,left,right):
    # 出口
    if left>=right:
        return arr
    # 找到基准数
    key = arr[left]
    low = left
    high = right
    while left<right:

        # 找到又边数小于左边数就交换，找不到就一走从右边向左边走着
        while left<right and key<=arr[right]:
            # 小兵走着说明这个走的数据还在走着,停下来
            right-=1
        # 走到这里说明遇到看小于这个的基数的数据，交换左边走的位置
        arr[left]=arr[right]
        # 上面while是右边向左边走，现在是左边向右边走
        while left<right and key >=arr[left]:
            left+=1
        arr[right] = arr[left]
        # 基准数归位,此时right==left
    arr[right]=key
    # 递归实现左边和右边的递归，最后出来
    quick_sort(arr,low,left-1)
    quick_sort(arr,left+1,high)

    return arr





''''
 快速排序：
 1先找基数，基数从最左边找，然后从右边开始走遍历数据往左边走，如果没有小于这个基数的就一直走，
 到找到了小于基数的就停下来
 
 2然后左边的往右边走，若果没有比基数大的就一直走，找到比基数大的就停下来
 
 3将两个停下来的 数据进行交换，然后再循环上面2步骤
 4 最后在将基准数归位到这个right== left的位置
 5 不断进行递归
 6 返回数据
'''
''' try again go on '''
def quick_sort2(arr,left,right):
    # 有递归先写一个出口
    if (left>=right):
        return arr
    low =left
    high = right
    key =arr[left]
    while left<right:

        while left<right and key<arr[right]:
            right-=1
        while left<right and key>arr[left]:
            left+=1

        arr[left],arr[right] = arr[right],arr[left]

    arr[left] = key
    quick_sort2(arr,low,left-1)
    quick_sort2(arr,left+1,high)
    return arr







if __name__ == "__main__":
    arr=[1,90,80,39,20,41]
    print(quick_sort2(arr,0,len(arr)-1))

