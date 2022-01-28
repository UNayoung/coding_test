from itertools import combinations

def solution(orders, course):
    answer = []
    com = dict()
    orders_max = []
    for i in course:
        orders_max.append(0)
    for i in orders:
        for k in range(len(course)):
            if(len(i) >= course[k]):
                temp = list(map(''.join, combinations(i, course[k])))
                for j in temp:
                    temp2 = ''.join(sorted(j))
                    if(com.get(temp2)):
                        com[temp2] += 1
                        if(com[temp2] > orders_max[k]):
                            orders_max[k] = com[temp2]
                    else:
                        com[temp2] = 1
    for i in range(len(course)):
        if(orders_max[i] == 0):
            break
        for key, value in com.items():
            if(len(key) == course[i] and value == orders_max[i]):
                answer.append(key)
    answer.sort()
    return answer