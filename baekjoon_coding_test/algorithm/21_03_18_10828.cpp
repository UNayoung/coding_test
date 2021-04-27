//stack
/*#include <iostream>
#include <stack>
#include <string>
using namespace std;
int main() {
	int n; cin >> n;
	stack<int> s;
	for (int i = 0; i < n; i++) {
		string com; cin >> com;
		if (com == "push") {
			int x; cin >> x;
			s.push(x);
		}
		else if (com == "top") { 
			if (s.empty()) cout << -1 << "\n"; //비었으면 -1 출력 
			else cout << s.top() << "\n";
		}
		else if (com == "size") {
			cout << s.size() << "\n";
		}
		else if (com == "pop") {
			if (s.empty()) cout << -1 << "\n";
			else {
				cout << s.top() << "\n";
				s.pop();
			}
		}
		else if (com == "empty") {
			if (s.empty()) cout << 1 << "\n";
			else cout << 0 << "\n";
		}
	}
	return 0;
}*/

#include <iostream>
#include <stack>
#include <string>
using namespace std;
int main() {
	int n; cin >> n;
	stack<int> s;
	for(int i;i<n;i++) {
		string com; cin >> com;
		if(com == "push") {
			int num; cin >> num;
			s.push(num);			
		}
		else if(com == "pop") {
			if(s.empty()) {
				cout << -1 << "\n";
			}
			else {
				cout << s.top() << "\n";
				s.pop();
			}
		}
		else if(com == "size") {
			cout << s.size() << "\n";
		}
		else if(com == "empty") {
			if(s.empty()) cout<<1<<"\n";
			else cout<<0<<"\n";
		}
		else if(com == "top") {
			if(s.empty()) cout<<-1<<"\n";
			else cout<<s.top()<<"\n";
		}
	}
	return 0;
}
