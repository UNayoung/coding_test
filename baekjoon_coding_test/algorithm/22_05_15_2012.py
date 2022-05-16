def solution():
    n = int(input())
    complain = []
    result = 0
    for i in range(n):
        complain.append(int(input()))
    complain.sort()
    for i in range(1, n+1):
        result += abs(complain[i-1] - i)
    print(result)

solution()