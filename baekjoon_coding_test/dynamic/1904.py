import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    array = [0] * 1000001
    array[1] = 1
    array[2] = 2
    for i in range(3, n+1):
        array[i] = (array[i-1] + array[i-2]) % 15746
    print(array[n])

solution()

# 1 선택 or 00 선택