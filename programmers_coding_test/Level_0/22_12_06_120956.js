function solution(babbling) {
  var answer = 0;
  babbling.map((val) => {
    var temp = val;
    if (temp.slice(0, 3) == "aya" || temp.slice(-3) == "aya") {
      temp = temp.replace("aya", "");
    }
    if (temp.slice(0, 2) == "ye" || temp.slice(-2) == "ye") {
      temp = temp.replace("ye", "");
    }
    if (temp.slice(0, 3) == "woo" || temp.slice(-3) == "woo") {
      temp = temp.replace("woo", "");
    }
    if (temp.slice(0, 2) == "ma" || temp.slice(-2) == "ma") {
      temp = temp.replace("ma", "");
    }
    if (temp == "") {
      answer += 1;
    }
  });
  return answer;
}
