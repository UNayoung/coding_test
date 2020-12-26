def solution(s):
    answer = ''
    word = s.split(' ')
    count=0
    for i in word:
        if(count!=0):
            answer+=" "
        for j in range(0, len(i)):
            if(j%2==0):
                temp = ord(i[j])
                if(temp>=ord("a")):
                    temp-=ord("a")-ord("A")
                    answer+=chr(temp)
                else:
                    answer+=i[j]
            else:
                temp = ord(i[j])
                if(temp<ord("a")):
                    temp+=ord("a")-ord("A")
                    answer+=chr(temp)
                else:
                    answer+=i[j]
        count+=1
    return answer

print(solution("try hello world"))