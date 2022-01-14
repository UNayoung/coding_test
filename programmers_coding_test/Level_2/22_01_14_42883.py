def solution(number, k):
    answer = ''
    list = []
    for i in range(0, len(number)):
        list.append(int(number[i]))
    start = 0
    for i in range(len(number)-k-1, -1, -1):
        max_index = 0
        max = -1
        for j in range(start, len(number)-i):
            if(list[j] > max):
                max = list[j]
                max_index = j
        start = max_index + 1
        answer += str(list[max_index])
    return answer