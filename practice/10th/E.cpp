#include <iostream>
#include <vector>
#include <cmath>

//10회 E 우주개척(그래프와 dfs를 활용한)
int T;
int P;
std::vector<std::vector<int>> space(101, std::vector<int>(3, 0));
std::vector<int> graph[101];
std::vector<bool> visit(101, false);

void solve(){
    int x1, y1, r;
    int x2, y2;
    float distance;
    for(auto i{0}; i<P; ++i){
        x1 = space[i][0];
        y1 = space[i][1];
        r = space[i][2];
        for(int j{0}; j<P; ++j){
            if(i == j) continue;
            x2 = space[j][0];
            y2 = space[j][1];
            distance = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
            if(distance <= r){
                graph[i].push_back(j);
            }
        }
    }
}

int dfs(int start){
    int num{0};
    for(auto next : graph[start]){
        if(visit[next]) continue;
        visit[next] = true;
        dfs(next);
	}
    for(auto i{0}; i<P; ++i){
        if(visit[i]) ++num;
    }
    return num;
}

int main(){
    std::cin >> T;
    for(int t{0}; t<T; ++t){
        std::cin >> P;
        for(auto i{0}; i<P; ++i){
            for(int j{0}; j<3; ++j){
                std::cin >> space[i][j];
            }
        }
        solve(); //그래프 생성
        int re{0};
        for(int i{0}; i < P; ++i){
            std::fill(visit.begin(), visit.end(), false);
            visit[i] = true;
            re = std::max(dfs(i), re); //100번 탐사(완전 탐색)
        }
        std::cout << re <<'\n'; //답출력
        
        std::fill(visit.begin(), visit.end(), false); //visit 초기화
        for (int i{0}; i < 101; ++i) graph[i].clear();  // 그래프 초기화
        for (int i = 0; i < 101; ++i) std::fill(space[i].begin(), space[i].end(), 0); // 각 내부 벡터를 0으로 초기화

    }

    return 0;

}
