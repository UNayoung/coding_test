import itertools
import math
import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    two = n // 2
    one = n - two * 2
    answer = 0
    for _ in range(n - n // 2 - n % 2):
        temp = [1] * one + [2] * two
        per = len(set(list(itertools.permutations(temp))))
        answer += (per * (int(math.pow(2, two))))
        two -= 1
        one += 2
    print((answer + 1) % 10007)

solution()

# n = 5
# 1,1,1,1,1 -> n
# 2 1 1 1
# 2 2 1 -> n//2 + 1

# n = 4
# 1, 1, 1, 1 -> n
# 2, 1, 1
# 2, 2 -> n//2


# n = 7
# 1 1 1 1 1 1 1
# 2 1 1 1 1 1
# 2 2 1 1 1
# 2 2 2 1