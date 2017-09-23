# Author : July  Yang

def  maopao(lists):
    count = len(lists)
    for i in range(0,count):
        for j in range(i+1,count):
            if lists[i]> lists[j]:
                lists[i],lists[j] = lists[j],lists[i]

    return lists

if __name__ == '__main__':
    arr=[1,9,2,5,4]
    print(maopao(arr))







