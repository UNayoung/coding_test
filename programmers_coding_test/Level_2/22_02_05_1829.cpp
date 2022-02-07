#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

int visited[100][100] = { 0, };
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int temp = 1;

void dfs(vector<vector<int>> picture, int i, int j, int k) {
    for(int a=0;a<4;a++) {
        int nx = i + dx[a];
        int ny = j + dy[a];
        if(nx >= 0 && ny >= 0 && nx < picture.size() && ny < picture[0].size()) {
            if(picture[nx][ny] == 0) continue;
            if(visited[nx][ny] == 1) continue;
            if(picture[nx][ny] != k) continue;
            visited[nx][ny] = 1;
            temp++;
            dfs(picture, nx, ny, k);
        }
    }
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = -1;
    memset(visited, 0, sizeof(visited));
    for(int i=0;i<m;i++) {
        for(int j=0;j<n;j++) {
            if(picture[i][j] == 0) continue;
            if(visited[i][j] == 1) continue;
            number_of_area++;
            temp = 1;
            visited[i][j] = 1;
            dfs(picture, i, j, picture[i][j]);
            if(temp > max_size_of_one_area) {
                max_size_of_one_area = temp;
            }
        }
    }
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}