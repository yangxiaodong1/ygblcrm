def Binary_search(arr,key):
    min = 0
    max = len(arr)
    while True:
        center = int((min + max) / 2)

        if key < arr[center]:
            max = center -1

        elif key > arr[center]:
            min = center + 1
        elif key ==arr[center]:
            return center

if __name__=="__main__":
    arr = [23,457,676]
    print(Binary_search(arr,676))