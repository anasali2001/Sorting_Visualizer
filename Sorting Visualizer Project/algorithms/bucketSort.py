import time
from colors import *

def __concat_list(lists):
    arr = []
    for l in lists:
        for i in l:
            arr.append(i)
    return arr

def bucketSort(arr, drawData, timeTick):
    m = max(arr) + 1
    n = len(arr)

    lists = [[] for i in range(10)]
    for j in range(len(arr)):
        idx = int((10 * float(arr[j])) / m)
        lists[idx].append(arr[j])

    drawData(arr, [ORANGE for i in range(len(arr))])
    time.sleep(timeTick)
    drawData(__concat_list(lists), [ORANGE for i in range(len(arr))])
    time.sleep(timeTick)

    for i in range(len(lists)):
        for j in range(1, len(lists[i])):
            temp = lists[i][j]
            pos = j - 1
            while pos >= 0 and lists[i][pos] > temp:
                lists[i][pos + 1] = lists[i][pos]
                lists[i][pos] = temp
                pos -= 1
                drawData(__concat_list(lists), [ORANGE for i in range(len(arr))])
                time.sleep(timeTick)
