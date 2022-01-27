def solution(orders, course):
    answer = []
    orders.sort(key=len)
    for i in range(len(orders)-1):
        for j in range(i+1, len(orders)):
            true = True
            for k in orders[i]:
                if(orders[j].find(k) == -1):
                    true = False
                    break
            if(true):
                answer.append(orders[j])
                break
    answer.sort()
    return answer