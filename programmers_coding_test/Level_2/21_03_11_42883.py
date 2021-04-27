# import itertools
#
# def solution(number, k):
#     k = len(number) - k
#     arr = []
#     index = []
#     new_index = []
#     total = []
#     big_total = []
#     for i in range(len(number)-k+1):
#         temp = number[i:i+k]
#         big_total.append(int(temp))
#     start = str(max(big_total))
#     for i in number:
#         arr.append(i)
#     for i in range(arr.index(start[0]), len(number)):
#         index.append(i)
#     c_arr = list(itertools.combinations(index, k))
#     for i in c_arr:
#         if(i[0] == arr.index(start[0])):
#             new_index.append(i)
#     for i in new_index:
#         total_temp = []
#         for j in i:
#             total_temp.append(arr[j])
#         total.append(int(''.join(total_temp)))
#     return str(max(total))
#
# print(solution("1231234", 3))

# 자릿수별로 고정시키면서 뒤로 가기?

def solution(number, k):
    k = len(number) - k
    temp = 0
    answer = ''
    arr_list = list(number)
    for i in range(k, 0, -1):
        arr = arr_list[temp:len(number)-i+1]
        big = max(arr)
        answer += big
        temp = arr.index(big)+1+temp
    return answer

print(solution("1231234", 3))

# 테스트10 통과 못함