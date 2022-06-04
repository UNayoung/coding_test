def solution():
    n = int(input())
    have = list(map(int, input().split()))
    m = int(input())
    find = list(map(int, input().split()))
    for i in find:
        if i in have:
            print(1, end=' ')
        else:
            print(0, end=' ')

solution()