#include <iostream>
#include <vector>
 
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

int n, m;
V<string> tab;

bool visited[2001][2001];

int dir[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};

void dfs(int x, int y) {
    if(visited[x][y]) return;
    visited[x][y] = true;
    
    F(d, 4) {
        int xx = x + dir[d][0];
        int yy = y + dir[d][1];

        if(xx >= 0 && xx < n && yy >= 0 && yy < m) {
            if(tab[xx][yy] != '#') {
                dfs(xx, yy);
            }
        }
    }
}

signed main () {
    cin >> n >> m;
    F(i, n) {
        string s; cin >> s;
        tab.pb(s);
    }
    
    int sx, sy;
    int ex, ey;

    F(i, n) {
        F(j, m) {
            if(tab[i][j] == 'K') {
                sx = i;
                sy = j;
            }
            if(tab[i][j] == 'B') {
                ex = i;
                ey = j;
            } 
        }
    }

    dfs(sx, sy);
    if(visited[ex][ey])
        cout << "yes" << endl;
    else
        cout << "no" << endl;

}
