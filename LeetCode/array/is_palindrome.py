"""Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:"""


def is_palindrome(s):
    alpn = [char.lower() for char in s if char.isalnum()]
    start = 0
    end = len(alpn) - 1

    while start < end:
        if alpn[start] != alpn[end]:
            return False

        start += 1
        end -= 1

    return True


if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    # s = "tab a cat"
    print(is_palindrome(s))