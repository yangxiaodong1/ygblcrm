

def Binary_sort(arr,key):

    min = 0
    max = len(arr)-1

    while True:
        center = int((min + max)  / 2)
        if key<arr[center]:
            max = center -1
        elif key >arr[center]:
            min = center +1
        elif key == arr[center]:
            return center
if __name__=="__main__":
    arr = [2222,33,656]
    print(Binary_sort(arr,33))