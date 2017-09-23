
'''增量，插入排序'''

def shell_sort(arr):
    count = len(arr)

    group = int(count / 2)

    while group>0:
        for i in range(0,group):
            j =i+ group
            while j <count:
                k = j - group
                key = arr[j]
                while k>=0 and key<arr[k]:
                    arr[k+group] =arr[k]
                    k -=group
                arr[k+group] = key
                j+=group
        group = int(group / 2)
    return arr

#------------------
def shell_sort(arr):

    count = len(arr)
    group = int(count / 2)

    while group >0:
        for i in range(0,group):
            j=i+count
            while j<count:
                k =j-group
                key =arr[j]
                while k>=0 and key<arr[k]:
                    arr[k+group]=arr[k]
                    k -=group
                arr[k+group]=key
                j+=group
        group=int(group /2)




if __name__=='__main__':
    arr = [22,3,6,]
    print(shell_sort(arr))