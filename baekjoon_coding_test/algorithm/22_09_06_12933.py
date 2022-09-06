import sys


def solution():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        store = []
        home_x, home_y = map(int, input().split())
        for _ in range(n):
            store.append(list(map(int, input().split())))
        festival_x, festival_y = map(int, input().split())


solution()