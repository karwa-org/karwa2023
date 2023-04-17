#include <bits/stdc++.h>
 
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

struct edge {
    int u, v, w;
    bool operator < (const edge other) const {
        return this->w > other.w;
    }
};

V<edge> adj[1000001];
bool visited[1000001];

signed main () {
    cin >> n >> m;
    F(i, m) {
        int u, v, w; cin >> u >> v >> w;
        adj[u].pb({u, v, w});
        adj[v].pb({v, u, w});
    }
    
    priority_queue <edge> pq;

    pq.push({1, -1, 0});
    while(!pq.empty()) {
        edge curr = pq.top();
        pq.pop();


        if(!visited[curr.u]) {
            visited[curr.u] = true;
            
            if(curr.u == n) {
                cout << curr.w << endl;
                break;
            }

            F(i, S(adj[curr.u])) {
                if(!visited[adj[curr.u][i].v]) {
                    pq.push({adj[curr.u][i].v, -1, adj[curr.u][i].w + curr.w});
                }
            }
        }
    }

}
