import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    n, m, r = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    layer = min(n, m) // 2
    for _ in range(r):
        for i in range(layer):
            temp = deque([])
            for k in range(i, m-i-1):
                temp.append(arr[i][k])
            for k in range(i, n-i-1):
                temp.append(arr[k][m-i-1])
            for k in range(m-i-1, i, -1):
                temp.append(arr[n-i-1][k])
            for k in range(n-i-1, i, -1):
                temp.append(arr[k][i])
            temp.append(temp[0])
            temp.popleft()
            for k in range(i, m-i-1):
                arr[i][k] = temp.popleft()
            for k in range(i, n-i-1):
                arr[k][m-i-1] = temp.popleft()
            for k in range(m-i-1, i, -1):
                arr[n-i-1][k] = temp.popleft()
            for k in range(n-i-1, i, -1):
                arr[k][i] = temp.popleft()
    for i in arr:
        print(*i)

solution()