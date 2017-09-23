
'''最小大，中间值'''

def Binary_search(arr,key):
    min = 0
    max = len(arr)-1
    if key in arr:
        while True:
            center = int((min +max ) / 2)
            if key <arr[center]:
                max = center - 1
            elif key > arr[center]:
                min = center +1
            elif key == arr[center]:
                return center

if __name__=='__main__':
    arr = [2,44,56,9]
    print(Binary_search(arr,56))
