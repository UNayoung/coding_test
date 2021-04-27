//연결되어 있는 묶음이 몇 묶음 인지

/*#include <iostream>
#include <string.h> //초기 
#include <stdio.h>
#include <vector>
using namespace std;

int map[52][52];
int visited[52][52];
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, 1, -1};

void dfs(int y, int x) {
	visited[y][x] = 1;
	for(int i=0;i<4;i++) {
		int ny = y + dy[i];
		int nx = x + dx[i];
		if(map[ny][nx] ==1 && visited[ny][nx] == 0) {
			dfs(ny, nx);
		}
	}
}

int main() {
	int t;
	
	cin >> t;
	while(t--) {
		// byte 00000000
		// int 00000000 00000000 00000000 00000000  
		memset(map, 0, sizeof(map)); // 1 byte 단위로 초기화가 된다 
		memset(visited, 0, sizeof(visited));
		// 0이 아닌 다른 값으로 초기화하려면 fill함수 쓰거나 반복문 
		int m,n,k;
		int ret = 0;
		scanf(" %d %d %d", &m, &n, &k);
		for(int i=0;i<k;i++) {
			int x,y;
			scanf(" %d %d", &x, &y);
			map[y+1][x+1] = 1;
		}
		
		for(int i=1;i<=n;i++) {
			for(int j=1;j<=m;j++) {
				if(map[i][j] == 1 && visited[i][j] ==0) {
					ret++;
					dfs(i, j);
				}
			}
		}
		cout << ret;
	}	
	return 0;
}*/

#include <iostream>
#include <string.h>
using namespace std;
int ground[52][52];
int visited[52][52];
void dfs(int x, int y) {
	visited[y][x] = 1;
	if(ground[y-1][x] == 1 && visited[y-1][x] == 0) {
		dfs(x,y-1);
	}
	if(ground[y+1][x] == 1 && visited[y+1][x] == 0) {
		dfs(x,y+1);
	}
	if(ground[y][x-1] == 1 && visited[y][x-1] == 0) {
		dfs(x-1,y);
	}
	if(ground[y][x+1] == 1 && visited[y][x+1] == 0) {
		dfs(x+1,y);
	}
}
int main() {
	int r; cin >> r;
	for(int w=0;w<r;w++){
		int m,n,k; cin >> m >> n >> k;
		int result = 0;
		memset(ground, 0, sizeof(ground));
		memset(visited, 0, sizeof(visited));
		for(int i=0;i<k;i++) {
			int x,y; cin >> x >> y;
			ground[y+1][x+1] = 1;
		}
		for(int i=1;i<n+1;i++){
			for(int j=1;j<m+1;j++) {
				if(ground[i][j]==1 && visited[i][j]==0) {
					result += 1;
					dfs(j,i);
				}
			}
		}
		cout << result << "\n";
	}
	return 0;
}
