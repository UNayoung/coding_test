def solution(s, n):
    answer = ''
    resultList = []
    sToString = list(s)
    for i in range(0, len(sToString)):
        temp = ord(sToString[i])
        if(temp>=ord("A") and temp<=ord("Z")):
            temp+=n
            if(temp>ord("Z")):
                while True:
                    if(temp>=ord("A") and temp<=ord("Z")):
                        break
                    temp-=26
            resultList.append(chr(temp))
        elif(temp>=ord("a") and temp<=ord("z")):
            temp+=n
            if (temp > ord("z")):
                while True:
                    if (temp >= ord("a") and temp <= ord("z")):
                        break
                    temp -= 26
            resultList.append(chr(temp))
        else:
            resultList.append(sToString[i])
    answer = ''.join(resultList)
    return answer

print(solution("a B z", 4))