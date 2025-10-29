//Judge 1167 트리에서 가장 먼 두 노드의 거리(E)
#include <iostream>
#include <vector>

int T, N;
int re{0};
std::vector<int> graph[10000];

void dfs(int start, int num){
    re = std::max(re, num);
    for(auto next : graph[start]){
        dfs(next, num+1);
    }
}

int main() {
    std::cin >> T;
    int a, b;
    for(int i{0}; i<T; ++i){
        std::cin >> N;
        
        for(int i{0}; i<N-1; ++i){
            std::cin >> a >> b;
            graph[a].push_back(b);
            graph[b].push_back(a);
        }

        // for(int i{0}; i<N; ++i){
        //     if(graph[i].size() == 1){
        //         dfs(i, 1);
        //     }
        // }

        // for(int i{0}; i<10000; ++i){
        //     graph[i].clear();
        // }
        // re = 0;
            
        for (int i{1}; i <= N; ++i) {
        std::cout << "Node " << i << " : ";
        for (int j : graph[i]) {
            std::cout << j << " ";
        }
        std::cout << std::endl;
    }
    std::cout << "-----------------------" << '\n';
    }

    return 0;
}