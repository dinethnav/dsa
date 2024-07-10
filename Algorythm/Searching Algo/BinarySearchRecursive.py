def b_search(arr, target, start, end):
    if start > end or start > len(arr):
        return -1

    mid = (start + end) // 2
    mid_val = arr[mid]
    # print(mid_val)

    if target == mid_val:
        return mid

    if target < mid_val:
        return b_search(arr, target, start, mid - 1)

    if target > mid_val:
        return b_search(arr, target, mid + 1, end)

if __name__ == "__main__":
    arr = [1, 4, 6, 9, ]
    b_search(arr, 9, 0, len(arr) - 1)