def solution(record):
    answer = []
    name = dict()
    visit_log = []
    for i in record:
        temp = list(map(str, i.split()))
        if temp[0] == 'Enter':
            visit_log.append([temp[1], '들어왔습니다.'])
            name[temp[1]] = temp[2]
        elif temp[0] == 'Change':
            name[temp[1]] = temp[2]
        else:
            visit_log.append([temp[1], '나갔습니다.'])
    for i in visit_log:
        answer.append(name[i[0]] + '님이 ' + i[1])
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
