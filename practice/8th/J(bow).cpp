//8-J
#include <iostream>
#include <vector>
#include <map>

int N, M;
std::vector<int> graph[256];

void solve(){
    
}

int main() {
    
    std::cin >> N >> M;
    for(int i{0}; i<M; ++i){
        int win, loose;
        std::cin >> win >> loose;
        graph[win].push_back(loose);
    }
    
    return 0;
}

