#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main() {
    int n, k; cin >> n >> k;
    bool found = false;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    unordered_set<int> elements;
    for (int i = 0; i < n; i++) {
        if (elements.count(k - a[i])) {
            cout << "yes" << endl;
            exit(0); 
        }

        elements.insert(a[i]);
    }
    cout << "no" << endl;
}
