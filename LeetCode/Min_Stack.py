# min Stack
import collections


class MinStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, val: int) -> None:
        if self.q:
            min_ = min(self.q[-1][1], val)
        else:
            min_ = val

        self.q.append((val, min_))

    def pop(self) -> None:
        return self.q.pop()[0]

    def top(self) -> int:
        return self.q[-1][0]

    def getMin(self) -> int:
        return self.q[-1][1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(0)
    print(minStack.getMin())  # return 0
    minStack.pop()
    print(minStack.top())  # return 2
    print(minStack.getMin())
