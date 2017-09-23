

def Binary_search(arr,key):
    min = 0
    max = len(arr)-1

    while True:
        center = int((max+min) / 2)
        if key < arr[center]:
            max = center-1
        elif key >arr[center]:
            min = center +1
        elif key == arr[center]:
            return center
if __name__ == "__main__":
    arr = [90,9,20]
    print(Binary_search(arr,9))