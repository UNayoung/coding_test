def solution(info, query):
    answer = []
    for i in query:
        query_temp = i.split()
        count = 0
        print(query_temp)
        for j in info:
            info_temp = j.split()
            if query_temp[0] != '-' and query_temp[0] != info_temp[0]:
                continue
            if query_temp[2] != '-' and query_temp[2] != info_temp[1]:
                continue
            if query_temp[4] != '-' and query_temp[4] != info_temp[2]:
                continue
            if query_temp[6] != '-' and query_temp[6] != info_temp[3]:
                continue
            if query_temp[7] > info_temp[4]:
                continue
            print(info_temp)
            count += 1
        answer.append(count)
        print(answer)
    return answer