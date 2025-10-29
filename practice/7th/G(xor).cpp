#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <limits>
#include <climits>
#include <cstring>

//1163 7회 경시대회, G, XOR은 즐거워?

int T, N, M;
int arr[100001];

void solve(int s, int i, int j){

}

int main(){
    int S, I, J;

    std::cin >> T;
    std::cin >> N;
    
    for(int t{0}; t<T; ++t){
        for(int n{0}; n<N; ++n){
            std::cin >> arr[n];
        }
        std::cin >> M;
        for(int i{0}; i<M; ++i){
            std::cin >> S >> I >> J;
            solve(S, I, J);
        }
    }

    return 0;
}