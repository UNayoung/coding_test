def solution(citations):
    answer = 0
    for i in range(1, len(citations)+1):
        temp = 0
        for j in citations:
            if(j >= i):
                temp += 1
        if(temp >= i):
            answer = i
    return answer