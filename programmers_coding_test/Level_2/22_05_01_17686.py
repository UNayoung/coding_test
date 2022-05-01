def solution(files):
    answer = []
    for i in files:
        temp = []
        for j in range(len(i)):
            if i[j].isdigit():
                temp.append(i[:j])
                break
        print(temp)
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))