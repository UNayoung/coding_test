#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> graph[102];
int visited[102];
int dist[102];
queue<int> q;

void bfs(int cur) {
	visited[cur] = 1;
	q.push(cur);
	while(!q.empty()) {
		int pop = q.front();
		q.pop();
		for(int i=0;i<graph[pop].size();i++) {
			if(visited[graph[pop][i]] == 0) {
				q.push(graph[pop][i]);
				visited[graph[pop][i]] = 1;
				dist[graph[pop][i]] = dist[pop] + 1;
			}
		}
	}
}

int main() {
	int n; cin >> n;
	int n1,n2; cin >> n1 >> n2;
	int m; cin >> m;
	for(int i=0;i<m;i++) {
		int a,b; cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}
	bfs(n1);
	if(dist[n2] == 0) {
		cout << -1;
	}
	else {
		cout << dist[n2];
	}
	return 0;
}
