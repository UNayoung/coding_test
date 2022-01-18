import math

def lcm(a,b):
    return (a * b) // math.gcd(a,b)

def solution(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        temp = lcm(temp, arr[i])
    return temp