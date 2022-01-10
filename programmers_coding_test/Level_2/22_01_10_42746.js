function solution(numbers) {
    var answer = '';
    var pad_list = [];
    for(var i=0;i<numbers.length;i++) {
        pad_list.push({origin: numbers[i], padding: parseInt(String(numbers[i]).padEnd(4, String(numbers[i])))});
    }
    pad_list.sort(function(a, b) {
        return b["padding"] - a["padding"];
    });
    pad_list.forEach(element => {
        answer += String(element["origin"]);
    });
    if(answer[0] == '0') {
        return String(parseInt(answer));
    }
    return answer;
}