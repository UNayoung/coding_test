#include <iostream>
#include <vector>

using namespace std;

vector<int> graph[22];

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            int temp; cin >> temp;
            graph[i].push_back(temp);
        }
    }
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            cout << graph[i][j];
        }
    }
    return 0;
}