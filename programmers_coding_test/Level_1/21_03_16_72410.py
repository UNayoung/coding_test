def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    arr = []
    for i in new_id:
        if(i>='a' and i<='z'):
            arr.append(i)
        if(i.isdigit() == True):
            arr.append(i)
        if(i == '-' or i == '_' or i == '.'):
            arr.append(i)
    # 3단계
    arr_3 = []
    check = 0
    for i in arr:
        if(i=='.'):
            if(check == 0):
                arr_3.append(i)
            check = 1
        else:
            check = 0
            arr_3.append(i)
    # 4단계
    if(len(arr_3) != 0):
        if(arr_3[0] == '.'):
            arr_3.pop(0)
    if(len(arr_3) != 0):
        if(arr_3[len(arr_3)-1] == '.'):
            arr_3.pop(len(arr_3)-1)
    # 5단계
    if(len(arr_3) == 0):
        arr_3.append('a')
    # 6단계
    if(len(arr_3)>15):
        arr_3 = arr_3[0:15]
        if(arr_3[14] == '.'):
            arr_3.pop(14)
    # 7단계
    temp = arr_3[len(arr_3)-1]
    length = len(arr_3)
    if(length<=2):
        for i in range(3-length):
            arr_3.append(temp)
    answer = ''.join(arr_3)
    return answer

print(solution("z-+.^."))