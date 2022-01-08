function solution(sizes) {
    var weight = -1;
    var height = -1;
    for(var i=0;i<sizes.length;i++) {
        var max = Math.max(...sizes[i]);
        var min = Math.min(...sizes[i]);
        if(weight < max) {
            weight = max;
        }
        if(height < min) {
            height = min;
        }
    }
    return weight * height;
}