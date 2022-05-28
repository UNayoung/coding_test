import math

def solution():
    n, m = map(int, input().split())
    gcd = math.gcd(n, m)
    print(gcd)
    print(gcd*(n//gcd)*(m//gcd))

solution()