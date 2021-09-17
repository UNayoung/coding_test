def solution(lottos, win_nums):
    answer = []
    zero = lottos.count(0)
    lottos_list = lottos
    for i in range(0, zero):
        lottos_list.remove(0)
    temp = len(list(set(lottos) - set(win_nums))) + 1 + zero
    if temp > 5:
        bottom = 6
    else:
        bottom = temp
    temp2 = bottom - zero
    if temp2 < 2:
        top = 1
    else:
        top = temp2
    answer.append(top)
    answer.append(bottom)
    return answer

print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
