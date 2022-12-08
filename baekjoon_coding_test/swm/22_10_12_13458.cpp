#include <iostream>
#include <vector>

using namespace std;

int n;
int a[1000002];
int b;
int c;
long long result;

int main() {
    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> a[i];
    }
    cin >> b >> c;

    result += n;
    for(int i=0;i<n;i++) {
        if(b >= a[i]) {
            a[i] = 0;
            continue;
        } else {
            a[i] -= b;
        }
        result += int(a[i]/c);
        if((a[i]%c) != 0) {
            result += 1;
        }
    }
    
    cout << result;
    return 0;
}