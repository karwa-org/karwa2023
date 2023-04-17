#include <iostream>
#include <set>
#include <vector>
#include<algorithm>

#define int long long
#define P(x) {if (debug) cout << x << endl;}
#define H(x) P(#x << ": " << (x))
#define FR(i,a,b) for (int i=(a); i<(b); i++)
#define F(i,n) FR(i,0,n)
#define D(i,n) for (int i=(n); i-->0;)
#define S(s) (int)(s).size()
#define ALL(v) v.begin(), v.end()
#define MI(a,v) a = min(a,v)
#define MA(a,v) a = max(a,v)
#define V vector
#define pb push_back
#define mt make_tuple
 
using namespace std;
 
template<class T> ostream& operator<<(ostream& os, V<T> v) {
    F(i,S(v)) os<<(i?" ":"")<<v[i]; 
    return os;
}
 
const bool debug = 1;

int n, m, k;

string tab[1001][1001];
int sum[1001][1001];
int sum2[1001][1001];
set <string> orgs;

signed main () {
    cin >> n >> m >> k;
    
    F(i, n) {
        F(j, m) {
            string s; cin >> s;
            tab[i][j] = s;
        }
    }

    F(i, k) {
        string s; cin >> s;
        orgs.insert(s);
    }
    

    F(i, n) {
        F(j, m) {
            sum[i][j] = (!orgs.count(tab[i][j]) && tab[i][j] != "null");
            if(i > 0) sum[i][j] += sum[i-1][j];
            if(j > 0) sum[i][j] += sum[i][j-1];
            if(i >0 && j > 0) sum[i][j] -= sum[i-1][j-1];
            
            sum2[i][j] = (orgs.count(tab[i][j]));
            if(i > 0) sum2[i][j] += sum2[i-1][j];
            if(j > 0) sum2[i][j] += sum2[i][j-1];
            if(i >0 && j > 0) sum2[i][j] -= sum2[i-1][j-1];
        }
    }
    int maxi = 0;
    F(i, n) {
        int idx = 0;
        while(idx < m) {
            int l = idx;
            int r = m;
            while(l < r) {
                int mid = (l+r)/2;
                int s = sum[i][mid];
                if(idx > 0) s -= sum[i][idx-1];
                if(i > 0) s -= sum[i-1][mid];
                if(idx > 0 && i > 0) s += sum[i-1][idx-1];

                if(s == 0) {
                    l = mid+1;
                }
                else {
                    r = mid;
                }
            }
            l--;

            FR(j, idx, l+1) {
                int d = i;
                int u = n;
                while(d < u) {
                    int mid = (d+u)/2;
                    int s = sum[mid][j];
                    if(idx > 0) s -= sum[mid][idx-1];
                    if(i > 0) s -= sum[i-1][j];
                    if(idx > 0 && i > 0) s += sum[i-1][idx-1];
                    if(s == 0) {
                        d = mid +1;
                    }
                    else{
                        u = mid;
                    }
                }
                d--;
                //cout << i << " " << j << " " <<  (d - i + 1) * (j - idx + 1) << endl;
                int ans = sum2[d][j];
                if(i > 0) ans -= sum2[i-1][j];
                if(idx > 0) ans -= sum2[d][idx-1];
                if(i > 0 && idx > 0) ans += sum2[i-1][idx-1];
                maxi = max(maxi, ans);
            }
            idx = l+2;
        }
    }
    cout << maxi << endl;
}
