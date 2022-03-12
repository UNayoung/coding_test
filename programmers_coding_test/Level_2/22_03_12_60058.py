def solution(p):
    answer = ''
    u = ""
    temp1 = 0
    temp2 = 0
    for i in p:
        if i == "(":
            temp1 += 1
        if i == ")":
            temp2 += 1
        u += i
        if temp1 == temp2:
            break
    return answer

print(solution("(()())()"))