def bill(sale, emoti):
    answer = 0
    for i in emoti:
        answer += (i * (100-sale)/100)
    return answer

def solution(users, emoticons):
    emoticons.sort(reverse=True)
    emoticons_sale = [0] * len(emoticons)
    service_user = []
    purchase = 5400
    for i in users:
        if bill(i[0], emoticons) < i[1]:
            continue
        service_user.append(i)
    return [len(service_user), purchase]

print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))