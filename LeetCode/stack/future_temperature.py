import collections


def future_temp(temperatures):
    q = collections.deque()

    answer = [0 for _ in range(len(temperatures))]

    for i in range(len(temperatures)):
        if not q:
            q.append((temperatures[i], i))
        else:
            while q and temperatures[i] > q[-1][0]:
                top = q.pop()
                top_index = top[1]
                top_distance = i - top_index

                answer[top_index] = top_distance

            q.append((temperatures[i], i))

    return answer


if __name__ == "__main__":
    temperatures = [30, 38, 30, 36, 35, 40, 28]
    print(future_temp(temperatures))
