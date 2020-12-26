def solution(s):
    answer = False
    digit = s.isdigit()
    if(digit==True):
        if(len(s)==4 or len(s)==6):
            answer = True
    return answer

print(solution("1234"))