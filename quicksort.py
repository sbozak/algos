import sys

total_comparisons = 0

def quicksort(arr, a, b):
    global total_comparisons
    if b-a <= 1:
        return arr    
    else:
        total_comparisons = total_comparisons + b-a-1
        index_p = choosePivot(arr, a, b)
        new_index_p = partition(arr, a, b, index_p)
        quicksort(arr, a, new_index_p)
        quicksort(arr, new_index_p+1, b)
        return arr

def choosePivot(arr, a, b):
    return a

def choosePivotLast(arr, a, b):
    return b-1

def choosePivotMedian(arr, a, b):
    if b-1 == a or b == a:
        return a
    med = int((a+(b-1))/2)    
    if (arr[a] < arr[b-1] and arr[b-1] < arr[med]) or (arr[med] < arr[b-1] and arr[b-1] < arr[a]):
        return b-1
    if (arr[a] < arr[med] and arr[med] < arr[b-1]) or (arr[b-1] < arr[med] and arr[med] < arr[a]):
        return med
    return a
    
    
    
def partition(arr, a, b, index_p):
    if index_p != a:
        swap(arr, index_p, a)

    p = arr[a]
    i = a+1
    j = a+1
    for x in range(a+1, b):
        if arr[j] < p:
            swap(arr, i, j)
            i = i+1
        j = j+1
        
    swap(arr, i-1, a)
    return i-1

def swap(arr, i, j):
    x = arr[i]
    arr[i] = arr[j]
    arr[j] = x


    
    
a = []
for line in sys.stdin:
    a.append(int(line))

quicksort(a, 0, len(a))
print(total_comparisons)

