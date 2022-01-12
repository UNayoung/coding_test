def solution(s):
    list = s.split(" ")
    for i in range(0, len(list)):
        list[i] = int(list[i])
    answer = str(min(list)) + " " + str(max(list))
    return answer