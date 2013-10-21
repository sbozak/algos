import sys
import collections

RetVal = collections.namedtuple('RetVal', ['count', 'array'])


def merge_and_count(left_arr, right_arr):
    arr = []
    count = 0
    j = 0
    k = 0
    for i in range(len(left_arr) + len(right_arr)):
        if j == len(left_arr):
            arr.append(right_arr[k])
            k = k+1
        elif k == len(right_arr) or left_arr[j] < right_arr[k]:
            arr.append(left_arr[j])
            j = j+1
        else :
            arr.append(right_arr[k])
            k = k+1
            count = count + len(left_arr) - j
    return RetVal(count, arr)
    

def sort_and_count(arr):
    if int(len(arr)) < 2:
        return RetVal(0, arr)
    elif int(len(arr)) == 2:
        if arr[0] > arr[1]:
            return RetVal(1, [arr[1], arr[0]])
        return RetVal(0, arr)
    else:
        left = sort_and_count(arr[0:int(len(arr)/2)])
        right = sort_and_count(arr[int(len(arr)/2):])
        split = merge_and_count(left.array, right.array)
        return RetVal(left.count + right.count + split.count, split.array)

a = []
for line in sys.stdin:
    a.append(int(line))

ret = sort_and_count(a)
print(ret.count)

