"""
Longest Substring Without Duplicates
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
"""


def longest_sstring(s):
    if len(s) < 2:
        return len(s)

    sub = set([s[0]])

    l = 0
    r = 1

    max_len = 1

    while r < len(s):
        char = s[r]

        if char not in sub:
            sub.add(char)
            max_len = max(max_len, (r - l + 1))
            r += 1

        else:
            while s[l] != char:
                sub.discard(s[l])
                l += 1
            l += 1
            r += 1

    return max_len


if __name__ == "__main__":
    print(longest_sstring(s="zxyzxyz"))
    print(longest_sstring(s="x"))
