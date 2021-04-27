# def solution(name):
#     answer = 0
#     return answer
#
# print(solution("JAN"))

def main():
    num = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    result = (len(arr)-1) // (num[1]-1)
    if((len(arr)-1) % (num[1]-1) != 0):
        result += 1
    print(result)

    # arr_min = min(arr)
    # middle = arr.index(arr_min)
    # if(middle == 0 or middle == len(arr)-1):
    #     length = (len(arr)-1) // (num[1]-1)
    #     if((len(arr)-1) % (num[1]-1) != 0):
    #         length += 1
    #     print(length)
    # else:
    #     length = 1
    #     left = middle - 1
    #     right = len(arr) - middle - 2
    #     temp = left // (num[1]-1)
    #     if(left % (num[1]-1) != 0):
    #         temp += 1
    #     length += temp
    #     temp = right // (num[1]-1)
    #     if(right % (num[1]-1) != 0):
    #         temp += 1
    #     length += temp
    #     print(length)

main()