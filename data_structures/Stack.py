"""python list is a dynamic array. so using list as python not recommended"""

from collections import deque

if __name__ == '__main__':
    stack = deque()
    stack.append(1)
    stack.append(2)
    print(stack.pop())
    print(stack)

