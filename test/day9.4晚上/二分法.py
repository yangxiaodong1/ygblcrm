def BinarySearch(arr,key):
    min = 0
    max = len(arr)

    if key in arr:
        while True:
            center = int((min + max) / 2)
            if key<arr[center]:
                max = center-1
            elif key > arr[center]:
                min = center +1
            elif key == arr[center]:
                return center
    else:
        print('没有这个数字')

if __name__=="__main__":
    arr =[90,3,8,9]
    print(BinarySearch(arr,8))