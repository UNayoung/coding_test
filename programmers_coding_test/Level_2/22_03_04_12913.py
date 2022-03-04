def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += (max(land[i-1][0:j] + land[i-1][j+1:4]))
    return max(land[len(land)-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))