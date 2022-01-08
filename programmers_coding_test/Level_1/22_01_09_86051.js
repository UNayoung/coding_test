function solution(numbers) {
    var answer = 0;
    var list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    for(var i=0;i<numbers.length;i++) {
        var index = list.indexOf(numbers[i]);
        list.splice(index, 1);
    }
    for(var i=0;i<list.length;i++) {
        answer += list[i];
    }
    return answer;
}