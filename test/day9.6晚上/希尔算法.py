
'''增量，快速插入'''

def shell_sort(arr):
    count = len(arr)
    group = int(count / 2)
    while group > 0:
        for i in range(0,group):
           j = i + group
           while j< count:
               k = j - group
               key  =arr[j]
               while k >=0 and key < arr[k]:
                   arr[k+group] = arr[k]
                   k -=group
               arr[k + group] = key
               j+=group
        group = int(group / 2)
    return arr

if __name__=="__main__":
    arr =[3,54,4]
    print(shell_sort(arr))

