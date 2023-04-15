#include <iostream>
#include <vector>

#define int long long
using namespace std;

signed main() {
    int n, k; cin >> n >> k;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] + a[j] == k) {
                cout << "yes" << endl;
                exit(0);
            }
        }
    }
    cout << "no" << endl;

}
