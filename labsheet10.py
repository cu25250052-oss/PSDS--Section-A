def digit_sum(n):
    n = abs(n)
    s = 0

    while n > 0:
        s += n % 10
        n //= 10

    return s


def solve(N, nums):

    frequency = {}
    answer = 0

    for num in nums:

        s = digit_sum(num)

        if s in frequency:
            answer += frequency[s]

        frequency[s] = frequency.get(s, 0) + 1

    return answer


N = int(input())
nums = list(map(int, input().split()))

print(solve(N, nums))