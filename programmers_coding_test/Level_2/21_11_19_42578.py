from itertools import combinations

def solution(clothes):
    answer = 1
    clothes_dict = dict()
    for i in clothes:
        if i[1] in clothes_dict:
            clothes_dict[i[1]].append(i[0])
        else:
            clothes_dict[i[1]] = [i[0]]

    n_list = list(clothes_dict)
    for i in n_list:
        answer *= (len(clothes_dict[i]) + 1)

    return answer - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))


# 시간초과
# from itertools import combinations
#
# def solution(clothes):
#     answer = 0
#     clothes_dict = dict()
#     for i in clothes:
#         if i[1] in clothes_dict:
#             clothes_dict[i[1]].append(i[0])
#         else:
#             clothes_dict[i[1]] = [i[0]]
#
#     n_list = list(clothes_dict)
#     n = len(clothes_dict)
#     for i in range(1, n + 1):
#         c = list(combinations(n_list, i))
#         for j in c:
#             temp = 1
#             for k in j:
#                 temp *= len(clothes_dict[k])
#             answer += temp
#
#     return answer
#
# print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))