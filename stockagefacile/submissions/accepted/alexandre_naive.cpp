#include <iostream>

using namespace std;

const int mod = 1e9 + 7;

int main() {
    int n; cin >> n;
    int x, y; x = y = 1;
    for (int i = 2; i <= n; i++) {
        int temp = x;
        x = (x + y) % mod;
        y = temp;
    }
    cout << x << endl;
}