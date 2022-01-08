function divisor(num) {
    var count = 0;
    if(num == 1) {
        return false;
    }
    if(num == 2) {
        return true;
    }
    for(var i=1;i<num/2 + 1;i++) {
        if(i*i>num) break;
        if(num%i == 0) {
            if(num/i == i) {
                count += 1;
            }
            else {
                count += 2;
            }
        }
    }
    if(count%2 != 0) {
        return false;
    }
    return true;
}

function solution(left, right) {
    var answer = 0;
    for(var i=left;i<right+1;i++) {
        if(divisor(i)) {
            answer += i;
        } else {
            answer -= i;
        }
    }
    return answer;
}


solution(1,10);

/*function divisor(num) {
    var count = 0;
    for(var i=1;i<num + 1;i++) {
        if(num%i == 0) {
            console.log(i);
            count += 1;
        }
    }
    if(count%2 != 0) {
        return false;
    }
    return true;
}

function solution(left, right) {
    var answer = 0;
    for(var i=left;i<right+1;i++) {
        console.log("\n" + i);
        console.log(divisor(i));
        if(divisor(i)) {
            answer += i;
        } else {
            answer -= i;
        }
    }
    console.log(answer);
    return answer;
}

solution(1,10);*/