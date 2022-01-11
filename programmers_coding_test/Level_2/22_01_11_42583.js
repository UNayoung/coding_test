function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    var ing = [];
    for(var i=0;i<bridge_length;i++) {
        ing.push(0);
    }
    while(true) {
        var sum = 0;
        for(var i=0;i<ing.length;i++) {
            sum += ing[i];
        }
        if(truck_weights.length == 0 && sum == 0) break;
        answer += 1;
        if(sum - ing[0] + truck_weights[0] <= weight) {
            ing.shift();
            ing.push(truck_weights[0]);
            truck_weights.shift();
        } else {
            ing.shift();
            ing.push(0);
        }
    }
    return answer;
}