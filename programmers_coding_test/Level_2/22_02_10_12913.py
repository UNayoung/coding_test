def solution(land):
    answer = 0
    option = [0,1,2,3]
    if(len(land) == 1):
        return max(land[0])
    for i in range(len(land)):
        if(i == len(land)-1):
            last = []
            for k in option:
                last.append(land[i][k])
            answer += max(last)
            break
        big = 0
        location = 0
        for j in option:
            temp = land[i+1]
            del temp[j]
            if(land[i][j]+max(temp) > big):
                big = land[i][j]+max(temp)
                location = j
        answer += land[i][location]
        option = [0,1,2,3]
        option.remove(location)
    return answer