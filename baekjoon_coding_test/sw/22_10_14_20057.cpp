#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> graph[100];

int main() {
    int n; cin >> n;
    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            int tmp; cin >> tmp;
            graph[i].push_back(tmp);
        }
    }
    for(int i=0;i<n;i++) {
        sort(graph[i].begin(), graph[i].end());
    }
    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            cout << graph[i][j];
        }
        cout << endl;
    }
    return 0;
}