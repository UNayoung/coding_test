//queue
/*#include <iostream>
#include <queue>
#include <string>
using namespace std;
int main() {
	int n;	cin >> n;
	queue<int> q;
	for (int i = 0; i < n; i++) {
		string com; cin >> com;
		if (com == "push") {
			int x; cin >> x;
			q.push(x);
		}
		else if (com == "pop") {
			if (q.empty()) cout << "-1" << "\n";
			else {
				cout << q.front() << "\n";
				q.pop();
			}
		}
		else if (com == "size") {
			cout << q.size() << "\n";
		}
		else if (com == "empty") {
			if (q.empty()) cout << 1 << "\n";
			else cout << 0 << endl;
		}
		else if (com == "front") {
			if (q.empty()) cout << -1 << "\n";
			else cout << q.front() << "\n";
		}
		else if (com == "back") {
			if (q.empty()) cout << -1 << "\n";
			else cout << q.back() << "\n";
		} //제일 최근에 추가된 원소
	}
	return 0;
}*/

#include <iostream>
#include <queue>
#include <string>
using namespace std;
int main() {
	int n; cin>>n;
	queue<int> q;
	for(int i;i<n;i++) {
		string com; cin>>com;
		if(com == "push") {
			int num; cin>>num;
			q.push(num);
		}
		else if(com == "pop") {
			if(q.empty()) cout<<-1<<"\n";
			else {
				cout<<q.front()<<"\n";
				q.pop();
			}
		}
		else if(com == "size") cout<<q.size()<<"\n";
		else if(com == "empty") {
			if(q.empty()) cout<<1<<"\n";
			else cout<<0<<"\n";
		}
		else if(com == "front") {
			if(q.empty()) cout<<-1<<"\n";
			else cout<<q.front()<<"\n";
		}
		else if(com == "back") {
			if(q.empty()) cout<<-1<<"\n";
			else cout<<q.back()<<"\n";
		}
	}
	return 0;
}
