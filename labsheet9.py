def solve(N, A):
    total_sum = sum(A)

    if total_sum > 0:
        return -1

    operations = -total_sum

    positive_sum = 0
    negative_sum = 0

    for value in A:
        if value > 0:
            positive_sum += value
        elif value < 0:
            negative_sum += abs(value)

    if positive_sum > operations:
        return -1

    if 2 * positive_sum > negative_sum:
        return -1

    return operations


def main():
    # Read ALL input at once
    data = list(map(int, input().split()))

    # If you are entering something like:
    # 1 -1
    # then treat it as an array of 2 elements.

    if len(data) == 2:
        A = data
        N = len(A)

        answer = solve(N, A)
        print(answer)
        return

    # Otherwise use the normal format:
    # T
    # N
    # A1 A2 A3 ...

    T = data[0]

    for _ in range(T):
        N = int(input())

        A = []
        while len(A) < N:
            A.extend(map(int, input().split()))

        A = A[:N]

        answer = solve(N, A)
        print(answer)


if __name__ == "__main__":
    main()