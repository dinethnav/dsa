import collections


def valid_bracket(string):
    q = collections.deque()

    open_b = {"{", "(", "["}

    close_b = {"}": "{",
               ")": "(",
               "]": "["}

    for i in string:
        if i in open_b:
            q.append(i)

        else:
            if q and q[-1] == close_b[i]:
                q.pop()
            else:
                return False

    if q:
        return False
    else:
        return True


if __name__ == "__main__":
    print(valid_bracket(")"))
    print(valid_bracket("()([])"))
