list = [25, 56, 78, 12, 4, 7, 22, 90, 23]

list.sort()
print(list)

# binary search

def binarySearch(list, key, start, end):
    mid = (start + end) / 2
    if(mid == key):
        print("found")
        return
    elif(mid > key):
        start = mid - 1
        binarySearch(list, key, start, end)
    else:
        end = mid + 1
        binarySearch(list, key, start, end)
    print("not found")

while(1):
    key = int(input("You want to Search: "))
    n = len(list)
    start = 0
    end = n - 1
    binarySearch(list, key, start, end)