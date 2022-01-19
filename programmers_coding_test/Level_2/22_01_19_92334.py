def solution(id_list, report, k):
    answer = []
    report_list = dict()
    for i in report:
        temp = i.split()
        if(report_list.get(temp[1])):
            report_list[temp[1]].append(temp[0])
            report_list[temp[1]] = list(set(report_list[temp[1]]))
        else:
            report_list[temp[1]] = [temp[0]]
    mail_list = dict()
    for i in report_list:
        if(len(report_list[i]) >= k):
            for j in report_list[i]:
                if(mail_list.get(j)):
                    mail_list[j] += 1
                else:
                    mail_list[j] = 1
    for i in id_list:
        if(mail_list.get(i)):
            answer.append(mail_list[i])
        else:
            answer.append(0)
    return answer