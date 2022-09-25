def cal_date(today, date, valid):
    t1, t2, t3 = today.split('.')
    d1, d2, d3 = date.split('.')
    temp, new_d2 = divmod(int(d2)+valid, 12)
    new_d1 = int(d1) + temp
    if new_d2 == 0:
        new_d1 -= 1
        new_d2 = 12
    if int(t1) > new_d1:
        return True
    if int(t1) == new_d1 and int(t2) > new_d2:
        return True
    if int(t1) == new_d1 and int(t2) == new_d2 and int(t3) > int(d3)-1:
        return True
    return False

def solution(today, terms, privacies):
    answer = []
    terms_dict = dict()
    for i in terms:
        a, b = i.split()
        terms_dict[a] = int(b)
    for i in range(len(privacies)):
        date, terms_type = privacies[i].split()
        temp = cal_date(today, date, terms_dict[terms_type])
        if temp:
            answer.append(i+1)
    return answer

print(solution(
"2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))