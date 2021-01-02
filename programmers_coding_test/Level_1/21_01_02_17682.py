def solution(dartResult):
    answer = 0
    score = {}
    index = 0
    before = 0
    option = 0
    ten = 0
    for i in dartResult:
        if (ten == 2):
            before = 10
        if (i == "S" or i == "D" or i == "T"):
            if (i == "S"):
                score[index] = before
            elif (i == "D"):
                score[index] = pow(before, 2)
            else:
                score[index] = pow(before, 3)
            index += 1
            ten = 0
        elif (i == "*" or i == "#"):
            option += 1
            if (len(score) == 1):
                if (i == "*"):
                    score[index-1] = score[index-1]*2
                else:
                    score[index-1] = score[index-1]*option*(-1)
            else:
                if (i == "*"):
                    score[index-1] = score[index-1]*2
                    score[index-2] = score[index-2]*2
                else:
                    score[index-1] = score[index-1]*option*(-1)
        else:
            ten += 1
            before = int(i)
            option = 0
    for i in range(0, len(score)):
        answer += score[i]
    return answer

print(solution("1D2S3T*"))