function solution(priorities, location) {
    var answer = 1;
    var list = [];
    for(var i=0;i<priorities.length;i++) {
        list.push([priorities[i], i]);
    }
    while(true) {
        var max = -1;
        for(var i=0;i<list.length;i++) {
            if(list[i][0] > max) {
                max = list[i][0];
            }
        }
        if(list[0][0] >= max) {
            if(list[0][1] == location) {
                break;
            } else {
                list.shift();
                answer += 1;
            }
        } else {
            list.push(list[0]);
            list.shift();
        }
    }
    return answer;
}