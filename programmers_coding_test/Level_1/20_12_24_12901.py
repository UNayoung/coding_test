def solution(a, b):
    answer = ''
    if(a==1):
        week=["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
        answer = week[b % 7-1]
    elif(a==2):
        week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
        answer = week[b % 7-1]
    elif(a==3):
        week = ["TUE", "WED", "THU", "FRI", "SAT", "SUN", "MON"]
        answer = week[b % 7-1]
    elif(a==4):
        week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
        answer = week[b % 7-1]
    elif(a==5):
        week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
        answer = week[b % 7-1]
    elif(a==6):
        week = ["WED", "THU", "FRI", "SAT", "SUN", "MON", "TUE"]
        answer = week[b % 7-1]
    elif(a==7):
        week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
        answer = week[b % 7-1]
    elif (a == 8):
        week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
        answer = week[b % 7-1]
    elif (a == 9):
        week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
        answer = week[b % 7-1]
    elif (a == 10):
        week = ["SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"]
        answer = week[b % 7-1]
    elif (a == 11):
        week = ["TUE", "WED", "THU", "FRI", "SAT", "SUN", "MON"]
        answer = week[b % 7-1]
    elif (a == 12):
        week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
        answer = week[b % 7-1]
    return answer

print(solution(5,24))