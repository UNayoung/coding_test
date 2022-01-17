def solution(arr1, arr2):
    answer = []
    arr1_width = len(arr1[0])
    arr1_height = len(arr1)
    arr2_width = len(arr2[0])
    for i in range(0, arr1_height):
        temp_answer = []
        for j in range(0, arr2_width):
            temp_sum = 0
            for k in range(0, arr1_width):
                temp_sum += arr1[i][k] * arr2[k][j]
            temp_answer.append(temp_sum)
        answer.append(temp_answer)
    return answer