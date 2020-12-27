def solution(phone_number):
    toString = list(phone_number)
    for i in range(0, len(phone_number)-4):
        toString[i] = '*'
    return ''.join(toString)

print(solution("01033334444"))