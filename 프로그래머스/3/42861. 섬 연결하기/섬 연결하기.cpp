#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> parent;
//Parent를 거슬러 올라가며 구하고, 도중에 연결돼있는데 통일이 안된경우 연결시킴
int getParent(int node)
{
    if(node == parent[node])
        return node;
    else
        return parent[node] = getParent(parent[node]);
}
//두 노드의 parent를 낮은쪽으로 합침
void UnionParent(int a, int b)
{
    a = getParent(a);
    b = getParent(b);
    if(a < b)
        parent[b] = a;
    else
        parent[a] = b;
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    //costs를 인덱스 2 기준으로 오름차순 정렬
    sort(costs.begin(),costs.end(),[](const vector<int> &a, const vector<int> &b)
        {
            return a[2] < b[2];
        });
    //Parent배열 초기화
    parent.resize(n);
    for(int i = 0; i < n; i++)
        parent[i] = i;
    //비용이 낮은 순서대로 연결(다른 parent일 경우만)
    int edge_used = 0;
    for(const auto & edge : costs)
    {
        int u = edge[0];
        int v = edge[1];
        int cost = edge[2];
        if(getParent(u) != getParent(v))
        {
            answer += cost;
            //그리고 Union 수행
            UnionParent(u,v);
            edge_used++;
        }
        //모든 노드가 연결돼면 Union종료
        if(edge_used == n-1)
            break;
    }
    return answer;
}