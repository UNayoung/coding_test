# Nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# def change(n,i):
#     str1 = ""
#     while n != 0:
#         if n % i == 0:
#             str1 += "0"
#         else:
#             str1 += str(Nums[n%i])
#         n = n // i
#     return(str1)[::-1]

# def solution(n):
#     answer = 0
#     tenToThree = change(n, 3)
#     turn = ""
#     for i in reversed(range(0, len(tenToThree))):
#         turn = turn+tenToThree[i]
#     answer = int(turn, 3)
#     return answer
#
# print(solution(125))

def solution(n):
    answer = 0
    arr = []
    while True:
        arr.append(str(n % 3))
        n = n//3
        if n == 0:
            break
    answer = ''.join(arr)
    answer = int(answer, 3)
    return answer

print(solution(45))