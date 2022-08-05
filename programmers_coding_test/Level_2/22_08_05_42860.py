def solution(name):
    answer = 0
    current = ['A'] * len(name)
    cursor = 0
    while ''.join(current) != name:
        temp = abs(ord(current[cursor])-ord(name[cursor]))
        if temp <= 13:
            answer += temp
        else:
            answer += (26-temp)
        current[cursor] = name[cursor]
        cursor += 1
    return answer

print(solution("JEROEN"))

# chr(45) -> 숫자에 해당하는거 반환
# ord('A') -> 아스키 코드 반환