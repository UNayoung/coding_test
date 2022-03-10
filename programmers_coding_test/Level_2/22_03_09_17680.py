def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities * 5)
    for i in cities:
        if i.lower() in cache:
            temp = cache.index(i.lower())
            cache.append(i.lower())
            cache.pop(temp)
            answer += 1
        else:
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(i.lower())
            answer += 5
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))