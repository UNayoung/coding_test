def solution(cacheSize, cities):
    answer = 0
    cache = []
    fre = []
    if cacheSize == 0:
        return len(cities * 5)
    for i in cities:
        if i.lower() in cache:
            answer += 1
            fre[cache.index(i.lower())] += 1
        else:
            if len(cache) >= cacheSize:
                temp = fre.index(min(fre))
                cache.pop(temp)
                fre.pop(temp)
            cache.append(i.lower())
            fre.append(0)
            answer += 5
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))