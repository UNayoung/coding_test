/*#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

vector<int> graph[102];
int visited[102];

int dfs(int cur) {
	int cnt = 1;
	visited[cur] = 1;
	for(int i=0;i<graph[cur].size();i++) {
		int next = graph[cur][i];
		if(visited[next] == 0){
			cnt += dfs(next);
		}
	}
	return cnt;
}

int main() {
	int n,m;
	cin >> n;
	cin >> m;
	for(int i=0;i<m;i++) {
		int a,b;
		scanf(" %d %d", &a, &b);
		graph[a].push_back(b);
		graph[b].push_back(a);
	}
	cout << dfs(1)-1;
	return 0;
}*/

#include <iostream>
#include <vector>
using namespace std;
vector<int> v[102];
int visited[102];
int result;
void dfs(int c) {
	visited[c] = 1;
	for(int i=0;i<v[c].size();i++) {
		if(visited[v[c][i]] == 0){
			result += 1;
			dfs(v[c][i]);
		}
	}
}
int main() {
	int com; cin >> com;
	int n; cin >> n;
	for(int i=0;i<n;i++) {
		int a,b; cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}
	dfs(1);
	cout << result;
	return 0;
}
