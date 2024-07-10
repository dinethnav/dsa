def b_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end and start < len(arr):

        mid = round((start + end) // 2)

        mid_val = arr[mid]

        if mid_val == target:
            return mid

        if mid_val < target:
            start = mid + 1

        if mid_val > target:
            end = mid

    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(b_search(arr, 5))
    print(b_search(arr,10))

    arr = [1]
    print(b_search(arr, 1))
