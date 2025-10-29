#include <iostream>
#include <vector>
#include <queue>
#define x first
#define y second 

int N;
int grid[51][51];
int dist[51][51];
std::queue<std::pair<int,int>> Q;

std::vector <int> dx = {-1, 0, 1, 0};
std::vector <int> dy = {0, 1, 0, -1};

void testprint(){
    std::cout << "--------------------------------------------" << '\n';
    for(int i{0}; i<N; ++i){
        for(int j{0}; j<N; ++j){
            std::cout << grid[i][j] << ' ';
        }
        std::cout << '\n';
    }
    std::cout << "dist" << "---------------------------" << '\n';
    for(int i{0}; i<N; ++i){
        for(int j{0}; j<N; ++j){
            std::cout << dist[i][j] << ' ';
        }
        std::cout << '\n';
    }
}

void solve(){
    if(grid[0][0] == 1){
        Q.push({0, 0});
        dist[0][0] = 1;
    }
    while(!Q.empty()){
        std::pair<int, int> cur = Q.front(); Q.pop();
        for(auto i{0}; i<4; ++i){
            int nx = cur.x + dx[i];
            int ny = cur.y + dy[i];
            if(nx < 0 || nx > N || ny < 0 || ny > N) continue;
            if(grid[nx][ny] == 0 || dist[nx][ny] > 0) continue;
            dist[nx][ny] = dist[cur.x][cur.y] + 1;
            Q.push({nx, ny});
        }
        
    }
    if(dist[N-1][N-1] == 0)
        std::cout << -1;
    else std::cout << (dist[N-1][N-1] - 3) * 3 + 2 << '\n';
    
}

int main() {
    std::cin >> N;
    for(int i{0}; i<N; ++i){
        for(int j{0}; j<N; ++j){
            std::cin >> grid[i][j];
        }
    }
    if(N == 1) std::cout << -1;
    else solve();
    //testprint();

    return 0;
}