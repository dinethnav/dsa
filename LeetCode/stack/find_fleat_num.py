"""
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.
"""

import collections


def find_fleat_num(position, speed, target):
    q = collections.deque()

    pos_time = []
    for i in range(len(position)):
        time = (target - position[i]) / speed[i]
        pos_time.append((position[i], time))

    pos_time = sorted(pos_time)

    for i in range(-1, -len(pos_time) - 1, -1):
        if not q:
            q.append(pos_time[i])

        else:
            if pos_time[i][1] > q[-1][1]:
                q.append(pos_time[i])

    return len(q)


if __name__ == "__main__":
    target = 10
    position = [4, 1, 0, 7]
    speed = [2, 2, 1, 1]

    print(find_fleat_num(position, speed, target))
