# Author : July  Yang 

def BinarySearch(arr,key):
    min = 0
    max = len(arr)-1
    if key in arr:
        center = int((min+max)/2)
        while True:
            if arr[center] > key:
                max = center -1
            elif arr[center] <key:
                min = center+1
            elif arr[center] == key:
                return center


if __name__ == "__main__":
    arr1 = [8,2,3,7,19,10]

    print(BinarySearch(arr1,3))




