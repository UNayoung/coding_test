#include <iostream>
#include <vector>

using namespace std;

vector<int> v[102];
int visited[102];
int total;

void dfs(int cur) {
	visited[cur] = 1;
	total += 1;
	for(int i=0;i<v[cur].size();i++) {
		if(visited[v[cur][i]] == 0) {
			dfs(v[cur][i]);
		}
	}
}

int main() {
	int n, m; cin >> n >> m;
	for(int i=0;i<m;i++) {
		int a, b; cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}
	dfs(1);
	cout << total-1;
	return 0;
}