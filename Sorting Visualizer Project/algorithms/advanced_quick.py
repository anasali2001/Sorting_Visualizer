from colors import *
def insertion_sort(arr, low, n):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j > low and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val
        drawData(arr, [WHITE if low == high or low == high + 1 else ORANGE for x in range(len(arr))])


def partition(arr, low, high):
    pivot = arr[high]
    i = j = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[high] = arr[high], arr[j]
    return j



def advanced_quick(arr, low, high):
    while low < high:

        if high - low + 1 < 10:
            insertion_sort(arr, low, high)
            break

        else:
            pivot = partition(arr, low, high)
            drawData(arr, [WHITE if low == high or low == high+1 else ORANGE for x in range(len(arr))] )

            if pivot - low < high - pivot:
                return hybrid_quick_sort(arr, low, pivot - 1)
                low = pivot + 1
            else:
                hybrid_quick_sort(arr, pivot + 1, high)
                high = pivot - 1
                return arr
    drawData(arr, [WHITE if low == high or low == high + 1 else ORANGE for x in range(len(arr))])