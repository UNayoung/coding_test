import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    hi = list(map(int, input().split()))
    ai = list(map(int, input().split()))
    answer = 0
    after = []

    for _ in range(n):
        cut = max(hi)
        answer += cut
        hi[hi.index(cut)] = 0
        for i in range(n):
            hi[i] += ai[i]
        print(answer)
        print(hi)
    print(answer)

solution()

# 1 3 2 4 6 - 1
# 3 10 5 8 7 - 7
# 5 17 8 12 8 - 8
# 7 24 11 16 9 - 16
# 9 31 14 20 10 - 31
