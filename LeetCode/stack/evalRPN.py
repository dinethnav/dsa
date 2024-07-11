import collections
def evalRPN(tokens):
    q = collections.deque()

    operations = {"*", "+", "-", "/"}
    answer = 0

    def operate(op, answer):
        eq = str(answer)

        while q:
            eq += op + q.pop()

        return eval(eq)

    for i in tokens:
        if i not in operations:
            q.append(i)

        else:
            answer = operate(i, answer)

    return answer


if __name__ == "__main__":
    tokens = ["1", "2", "+", "3", "*", "4", "-"]
    print(evalRPN(tokens))
