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

struct edge {
    int w;
    int u;
    int v;

    bool operator < (const edge other) const {
        return this->w < other.w;
    }
};

V<edge> edges;
int n, m; 

int p[100001];

int pfind(int x) {
    if(x == p[x]) return x;
    p[x] = pfind(p[x]);
    return p[x];
}

void punion(int a, int b) {
    a = pfind(a);
    b = pfind(b);

    p[a] = p[b];
}

int solve_threshold(int lambda){
    F(i, n+1) p[i] = i;

    int cost = 0;
    int c = 0;
    F(i, m) {
        if(edges[i].w >= lambda && pfind(edges[i].u) != pfind(edges[i].v)) {
            punion(edges[i].u, edges[i].v);
            cost += edges[i].w;
            c += 1;
        }
    }
    if(c == n-1) {
        return cost;
    }
    else {
        return 1000000000000000LL;
    }
}

signed main () {
    cin >> n >> m;
    F(i, m) {
        int u, v, w; cin >> u >> v >> w;
        edges.pb({w, u, v});
    }

    sort(ALL(edges));
    int baseline = solve_threshold(0);

    int lo = 0;
    int hi = n-1;

    while(lo < hi) {
        int mid = (lo+hi)/2; 
        int cost = solve_threshold(edges[mid].w);
        if(4*cost <= baseline*5) {
            lo = mid+1;
        }
        else {
            hi = mid;
        }
    }
    cout << edges[lo-1].w << endl;
}

