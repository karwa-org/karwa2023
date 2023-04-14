#include <bits/stdc++.h>
#define int long long
using namespace std;

bool comp(tuple<int,int,int> t1, tuple<int,int,int> t2) {
    return get<2>(t1) < get<2>(t2);
}

vector<int> parents;
vector<int> ranks;

int find(int x) {
    if (parents[x] == x) return x;
    parents[x] = find(parents[x]);
    return parents[x];
}

void union_(int x, int y) {
    x = find(x); y = find(y);
    if (x != y) {
        if (ranks[x] > ranks[y]) {
            parents[x] = y;
        }
        else if (ranks[y] > ranks[x]) {
            parents[y] = x;
        }
        else {
            parents[x] = y;
            ranks[x]++;
        }
    }
}

int kruskal(vector<tuple<int,int,int>> edges, int n, int alpha) {
    parents.resize(n);
    for (int i = 0; i < n; i++) {
        parents[i] = i;
    }
    ranks.resize(n, 0);
    int cost = 0;
    int comp = 0;
    for (auto [u,v,w] : edges) {
        if (w >= alpha && find(u) != find(v)) {
            union_(u,v); cost += w;
            comp++;
        }
    }
    return comp + 1 == n ? cost : LONG_LONG_MAX;
}

signed main() {
    int n, m; cin >> n >> m;
    vector<tuple<int,int,int>> edges;
    int mx = 0;
    for (int i = 0; i < m; i++) {
        int u,v, w; cin >> u >> v >> w;
        mx = max(mx, w);
        edges.push_back(make_tuple(--u,--v,w));
    }

    sort(edges.begin(), edges.end(), comp);

    int best = kruskal(edges, n, 0);
    int acceptable = (int) (((double) best) *1.25);
    int lo = 0; int hi = mx + 1;
    while (hi > lo) {
        int mid = lo + (hi - lo) / 2;
        int res = kruskal(edges, n, mid);
        if (res <= acceptable) {
            lo = mid + 1;
        }
        else {
            hi = mid;
        }
    }
    cout << lo - 1 << endl;

}
