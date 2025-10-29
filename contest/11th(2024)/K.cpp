//수정

#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

int N, F, E;
std::vector<std::tuple<int, int, int>> student;


int main(){
    std::cin >> N;  //전체수강생
    std::cin >> F;  //첫타자
    std::cin >> E;  //족보주는순서
    visit.resize(N+1, 0);
    visit[0]=1;
    visit[F]=1;

    int a, b, c;
    for(int i{0}; i<E; ++i){
        std::cin >> a >> b >> c;
        student.push_back(std::make_tuple(a, b, c));
    }
    return 0;
}