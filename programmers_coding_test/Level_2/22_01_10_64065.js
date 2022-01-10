function solution(s) {
    var answer = [];
    var temp = s.slice(2, s.length-2);
    var list = temp.split("},{");
    for(var i=0;i<list.length;i++) {
        list[i] = list[i].split(",");
    }
    list.sort(function(a, b) {
        return a.length - b.length;
    })
    answer.push(parseInt(list[0][0]));
    for(var i=1;i<list.length;i++) {
        var temp = list[i].filter(x => !list[i-1].includes(x));
        answer.push(parseInt(temp[0]));
    }
    return answer;
}