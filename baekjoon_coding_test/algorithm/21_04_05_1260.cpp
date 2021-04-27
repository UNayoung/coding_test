#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> graph[1002];
int visited_dfs[1002];
int visited_bfs[1002];
queue<int> q;

void dfs(int cur) {
	visited_dfs[cur] = 1;
	cout << cur << " ";
	for(int i=0;i<graph[cur].size();i++) {
		if(visited_dfs[graph[cur][i]] == 0) {
			dfs(graph[cur][i]);
		}
	}
}

void bfs(int cur) {
	visited_bfs[cur] = 1;
	q.push(cur);
	while(!q.empty()) {
		int front = q.front();
		q.pop();
		cout << front << " ";
		for(int i=0;i<graph[front].size();i++) {
			if(visited_bfs[graph[front][i]] == 0) {
				visited_bfs[graph[front][i]] = 1;
				q.push(graph[front][i]);
			}
		}
	}
}

int main() {
	int n,m,v;
	cin >> n >> m >> v;
	for(int i=0;i<m;i++) {
		int a,b;
		cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}
	for(int i=1;i<n+1;i++) {
		if(!graph[i].empty()) {
			sort(graph[i].begin(), graph[i].end());
		}
	}
	dfs(v);
	cout << "\n";
	bfs(v);
	return 0;
}
