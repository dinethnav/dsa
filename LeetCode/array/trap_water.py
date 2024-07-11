def trap(height):
    if len(height) < 2:
        return 0

    l = 0
    r = 1

    capacity = 0

    while r < len(height):
        print(l)

        filled = 0
        while r < len(height) and height[r] < height[l]:
            filled += height[r]
            r += 1

        if r == len(height):
            l += 1
            r = l + 1
            continue

        if r - l > 1:
            d = r - l - 1
            print(l, r, filled, d)
            capacity += min(height[l], height[r]) * d - filled

        l = r
        r += 1

    return capacity

# height = [0,2,0,3,1,0,1,3,2,1]
