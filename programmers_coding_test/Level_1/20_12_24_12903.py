def solution(s):
    answer = ''
    if len(s)%2 == 1:
        temp=len(s)-1
        temp=temp/2
        temp=int(temp)
        answer=s[temp]
    else:
        temp=len(s)/2
        temp=int(temp)
        answer=s[temp-1]
        answer=answer+s[temp]
    return answer

print(solution("qwer"))