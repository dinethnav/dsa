"""
Eating Bananas
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:

Input: piles = [1,4,3,2], h = 9

Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

Example 2:

Input: piles = [25,10,23,4], h = 4

Output: 25
"""


def get_rate(piles, h):
    def check(k):
        h_2_f = 0
        for pile in piles:
            h_2_f += round(pile / k + 0.5)

        return h_2_f

    min_rate = max(piles)
    start = 0
    end = len(piles) - 1

    arr = [i for i in range(1, min_rate + 1)]

    while start <= end:

        mid = (start + end) // 2

        k = arr[mid]

        h_f = check(k)

        if h_f > h:
            start = mid + 1

        if h_f <= h:
            min_rate = min(min_rate, k)
            end = mid - 1

    return min_rate


if __name__ == "__main__":
    print(get_rate(piles=[1, 4, 3, 2], h=9))
    print(get_rate(piles=[25, 10, 23, 4], h=4))
