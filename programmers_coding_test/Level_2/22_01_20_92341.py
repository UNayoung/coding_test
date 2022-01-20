import math

def solution(fees, records):
    answer = []
    car_list = dict()
    for i in records:
        temp = i.split()
        if(temp[2] == "IN"):
            if(car_list.get(temp[1])):
                car_list[temp[1]] = ["IN", temp[0], car_list[temp[1]][2]]
            else:
                car_list[temp[1]] = ["IN", temp[0], 0]
        else:
            time = (int(temp[0][0:2]) * 60 + int(temp[0][3:5])) - (int(car_list[temp[1]][1][0:2]) * 60 + int(car_list[temp[1]][1][3:5]))
            car_list[temp[1]] = ["OUT", temp[0], car_list[temp[1]][2] + time]
    car_list = dict(sorted(car_list.items()))
    for i in car_list:
        if(car_list[i][0] == "IN"):
            car_list[i][2] = car_list[i][2] + ((23 * 60 + 59) - (int(car_list[i][1][0:2]) * 60 + int(car_list[i][1][3:5])))
        if(car_list[i][2] <= fees[0]):
            answer.append(fees[1])
        else:
            money = fees[1] + math.ceil(((car_list[i][2] - fees[0]) / fees[2])) * fees[3]
            answer.append(money)
    return answer