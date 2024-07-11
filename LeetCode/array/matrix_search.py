def matrix_search(matrix, target):
    m, n = len(matrix), len(matrix[0])

    def row_search(start, end):

        mid = (start + end) // 2

        if start > end:
            return -1

        if matrix[mid][0] <= target <= matrix[mid][-1]:
            return mid

        if target > matrix[mid][-1]:
            return row_search(mid + 1, end)

        if target < matrix[mid][0]:
            return row_search(start, mid - 1)

    def col_search(r, start, end):
        mid = (start + end) // 2

        if start > end:
            return False

        cval = matrix[r][mid]

        if cval == target:
            return True

        if cval > target:
            return col_search(r, start, mid - 1)

        if cval < target:
            return col_search(r, mid + 1, end)

    r = row_search(0, m - 1)
    if r == -1:
        return False
    c = col_search(r, 0, n - 1)

    return c


if __name__ == "__main__":
    matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]

    print(matrix_search(matrix, 5))
    print(matrix_search(matrix, 11))
