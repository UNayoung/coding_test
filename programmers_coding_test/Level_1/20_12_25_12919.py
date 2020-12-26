def solution(seoul):
    answer = ''
    kim = seoul.index("Kim")
    answer = '김서방은 '+str(kim)+'에 있다'
    return answer

print(solution(["Jane", "Kim"]))