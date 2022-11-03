import sys

def solution():
    input = sys.stdin.readline
    t = int(input())
    array = [0] * 101
    array[0] = 1
    array[1] = 1
    array[2] = 1
    array[3] = 2
    array[4] = 2
    for i in range(5, 101):
        array[i] = array[i-1] + array[i-5]
    for _ in range(t):
        n = int(input())
        print(array[n-1])

solution()
