def solution(s):
    answer_list = []
    s_len = len(s)
    if len(s) == 1:
        return 1
    for i in range(1, s_len//2 + 1):
        result = ""
        count = 0
        temp = s[0:i]
        if s_len%i > 0:
            divide = s_len//i + 1
        else:
            divide = s_len//i
        for j in range(1, divide+1):
            if s[j*i-i:j*i] == temp:
                count += 1
                if j == divide:
                    result = result + str(count) + temp
            else:
                if count == 1:
                    result += temp
                    if j == divide:
                        result += s[j*i-i:j*i]
                else:
                    result = result + str(count) + temp
                    if j == divide:
                        result += s[j*i-i:j*i]
                count = 1
                temp = s[j*i-i:j*i]
        answer_list.append(len(result))
        if min(answer_list) <= i+2:
            break
    answer = min(answer_list)
    return answer

print(solution("aabbaccc"))