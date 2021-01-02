def toBinary(num, n):
    temp = []
    while True:
        temp.insert(0, num%2)
        num = num//2
        if (num==0):
            break
    if(len(temp)!=n):
        for i in range(0, n-len(temp)):
            temp.insert(0, 0)
    for i in range(0, n):
        temp[i] = str(temp[i])
    return ''.join(temp)

def solution(n, arr1, arr2):
    answer = []
    for i in range(0, n):
        arr1[i] = toBinary(arr1[i], n)
        arr2[i] = toBinary(arr2[i], n)
    for i in range(0, n):
        temp = ""
        for j in range(0, n):
            if(arr1[i][j]=="0" and arr2[i][j]=="0"):
                temp+=" "
            else:
                temp+="#"
        answer.append(temp)
    return answer

print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))