# genenrate prathesis

def generate_parenthesis(n):
    q = 0
    answer = []

    def create_pattern(open_c, close_c, q, tmp):
        # print(q , tmp,open_c,close_c)

        if open_c == 0 and close_c == 0:
            answer.append(tmp)

        if q > 0:
            if close_c > 0 and open_c > 0:

                create_pattern(open_c, close_c - 1, q - 1, tmp + ')')

                create_pattern(open_c - 1, close_c, q + 1, tmp + '(')

            elif open_c > 0:

                create_pattern(open_c - 1, close_c, q + 1, tmp + '(')

            elif close_c > 0:

                create_pattern(open_c, close_c - 1, q - 1, tmp + ')')

        if not q and open_c > 0:
            create_pattern(open_c - 1, close_c, q + 1, tmp + '(')

        return

    create_pattern(n, n, q, '')

    return answer
