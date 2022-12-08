import sys

def solution():
    input = sys.stdin.readline
    n, r = map(int, input().split())
    survivor = list(map(int, input().split()))
    if n == r:
        print('*')
        return 0
    for i in range(1, n+1):
        if i not in survivor:
            print(i, end=' ')
    return 0

solution()