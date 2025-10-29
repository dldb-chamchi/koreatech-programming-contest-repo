#include <iostream>
#include <vector>
#include <cmath>

int T;
int P;
std::vector<std::vector<int>> space(101, std::vector<int>(3, 0));
std::vector<int> graph[101];

void solve() {
    int x1, y1, r;
    int x2, y2;
    float distance;
    
    // 각 정점에 대해 그래프를 초기화
    for (int i = 0; i < P; ++i) {
        graph[i].clear(); // 매번 초기화
    }
    
    for (int i = 0; i < P; ++i) {
        x1 = space[i][0];
        y1 = space[i][1];
        r = space[i][2];
        for (int j = 0; j < P; ++j) {
            if (i == j) continue;
            x2 = space[j][0];
            y2 = space[j][1];
            distance = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
            if (distance <= r) {
                graph[i].push_back(j);
            }
        }
    }
}

int main() {
    std::cin >> T;
    for (int t = 0; t < T; ++t) {
        std::cin >> P;

        // space도 초기화
        space = std::vector<std::vector<int>>(P, std::vector<int>(3, 0));

        for (int i = 0; i < P; ++i) {
            for (int j = 0; j < 3; ++j) {
                std::cin >> space[i][j];
            }
        }

        solve();
        
        // 그래프 출력
        for (int i = 0; i < P; i++) {
            std::cout << "graph " << i << ": ";
            for (int j = 0; j < graph[i].size(); j++) {
                std::cout << graph[i][j] << " ";
            }
            std::cout << '\n';
        }
    }

    return 0;
}
