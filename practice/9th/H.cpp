#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <limits>
#include <climits>
#include <cstring>
#define x first
#define y second
//9th 초콜릿의 저주 H번

int M, N;
char map[6][6];
std::string s;
bool visit[15];
bool mapvisit[6][6];

std::queue<std::pair<int,int>> Q;
std::vector <int> dx = {-1, 0, 1, 0};
std::vector <int> dy = {0, 1, 0, -1};

void bfs(int idx){
    if(idx == s.length()) return;

    while(!Q.empty()){
        std::pair<int, int> cur = Q.front(); Q.pop();
        for(auto i{0}; i<4; ++i){
            int nx = cur.x + dx[i];
            int ny = cur.y + dy[i];
            if(nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
            if(visit[idx] || mapvisit[nx][ny]) continue;
            if(map[nx][ny] == 'X' || map[nx][ny] != s[idx]) continue;
            visit[idx]= true;
            mapvisit[nx][ny] = true;
            Q.push({nx, ny});
            bfs(idx+1);
            visit[idx] = false;
            mapvisit[nx][ny] = false;
        }
    }
}

int main(){

    std::cin >> s;
    std::cin >> M >> N;
    for(auto i{0}; i<M; ++i){
        for(auto j{0}; j<N; ++j){
            std::cin >> map[i][j];
        }
    }
    for(auto i{0}; i<M; ++i){
        for(auto j{0}; j<N; ++j){
            if(map[i][j] == s[0]){
                Q.push({i, j});
                mapvisit[i][j] = true;
                visit[0] = true; //첫문자
                bfs(1);
                mapvisit[i][j] = false;
                visit[0] = false;
            }
        }
    }
    //std::cout << s << '\n';
    //bfs();
    for(size_t i{0}; i<s.length(); ++i){
        std::cout << visit[i] << ' ';
    }
    std::cout << '\n';
    //testprint();

    return 0;
}