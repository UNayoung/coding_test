def solution(s):
    answer = True
    p1 = s.count("p")
    p2 = s.count("P")
    total_p = p1+p2
    y1 = s.count("y")
    y2 = s.count("Y")
    total_y = y1+y2
    if(total_p!=total_y):
        return False
    return True

print(solution("Pyy"))