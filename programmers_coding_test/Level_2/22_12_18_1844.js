function bfs(graph, n, m) {
  var queue = [[0, 0]];
  var dx = [-1, 1, 0, 0];
  var dy = [0, 0, -1, 1];
  while (queue.length != 0) {
    var temp = queue.shift();
    for (let i = 0; i < 4; i++) {
      var nx = temp[0] + dx[i];
      var ny = temp[1] + dy[i];
      if (nx < 0 || nx >= n || ny < 0 || ny >= m || graph[nx][ny] != 1)
        continue;
      queue.push([nx, ny]);
      graph[nx][ny] = graph[temp[0]][temp[1]] + 1;
    }
  }
}

function solution(maps) {
  var n = maps.length;
  var m = maps[0].length;
  bfs(maps, n, m);
  if (maps[n - 1][m - 1] == 1) return -1;
  return maps[n - 1][m - 1];
}
