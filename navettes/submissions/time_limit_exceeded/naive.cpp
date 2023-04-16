#include <iostream>


using namespace std;
int main() {
    int n, m; cin >> n >> m;
    int ans = 0;
    while (n > 0) {
        ++ans; n -= m;
    }
    cout << ans << endl;
}