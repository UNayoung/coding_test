function solution(people, limit) {
    var answer = 0;
    var left = 0;
    var right = people.length - 1;
    people.sort(function(a, b) {
        return b - a;
    });
    while(true) {
        if(left > right) break;
        if(left == right) {
            answer += 1;
            break;
        }
        if(people[left] + people[right] > limit) {
            left += 1;
        } else {
            left += 1;
            right -= 1;
        }
        answer += 1;
    }
    return answer;
}