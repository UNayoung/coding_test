import sys

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    dot = list(map(int, input().split()))
    dot.sort()
    for _ in range(m):
        start, end = map(int, input().split())
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if dot[mid] < start:
                left = mid + 1
            else:
                right = mid - 1
        first = left
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if dot[mid] > end:
                right = mid - 1
            else:
                left = mid + 1
        second = right + 1
        print(second - first)

solution()