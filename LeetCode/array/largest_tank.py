
def largest_tank(height):
    start = 0
    end =len(height) - 1
    max_area = 0

    while start < end:
        area = (end - start) * min(height[start], height[end])

        max_area = max(area, max_area)

        if height[start] > height[end]:
            end -= 1
        else:
            start += 1

    return max_area


if __name__ == "__main__":
    height = [1, 7, 2, 5, 4, 7, 3, 6]
    # height = [2,2,2]
    largest_tank(height)
