function solution(price, money, count) {
    var pay = 0;
    for(var i=1;i<count+1;i++) {
        pay += price * i;
    }
    var answer = pay - money;
    if(answer <= 0) {
        return 0;
    }
    return answer;
}