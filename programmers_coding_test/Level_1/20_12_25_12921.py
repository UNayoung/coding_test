# def sosu(n):
#     result = True
#     if(n==1):
#         return False
#     for i in range(2, n):
#         if(n%i==0):
#             return False
#     return result

def solution(n):
    num = set(range(2, n+1))
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)

print(solution(10))