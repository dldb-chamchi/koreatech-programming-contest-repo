#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <tuple>

int N, F, E;
std::vector<std::tuple<int, int, int>> student;
std::vector<bool> visit;

int testStuPrint(){
    std::cout << "-------stu------\n";
    for(int i{0}; i<E; ++i){
        std::cout << std::get<0>(student[i]) << ' ' << std::get<1>(student[i]) << ' ' << std::get<2>(student[i]) << '\n';
    }
    std::cout << "----------------\n";
}

int testVisitedPrint(){
    std::cout << "-------visit------\n";
    for(int i{0}; i<N+1; ++i){
        std::cout << visit[i] << ' ';
    }
    std::cout << "\n----------------\n";
}

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
    std::sort(student.begin(), student.end(), [](auto a, auto b){ return std::get<2>(a)<std::get<2>(b); });

    //testStuPrint();
    
    int A, B;
    for(int i{0}; i<E; ++i){
        A= std::get<0>(student[i]);
        B= std::get<1>(student[i]);
        // 원래 visit가 bool이었음
        // visit[B]+=visit[A];
        // visit[A]+=visit[B];
        visit[B] = visit[A] || visit[B];
        visit[A] = visit[A] || visit[B];
    }

    //testVisitedPrint();

    for(int i{0}; i<=N; ++i){
        if(visit[i]){
            std::cout << i << ' ';
        }
    }

    return 0;
}
