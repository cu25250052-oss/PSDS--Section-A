
def solve():
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))

        arr.sort(key=lambda x: ((x ^ k).bit_count(), x))

        print(*arr)


if __name__ == "__main__":
    solve()
