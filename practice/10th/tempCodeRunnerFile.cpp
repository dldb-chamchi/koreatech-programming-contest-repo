#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <limits>
#include <climits>
#include <cstring>

int T, N;
std::vector<int> S;

bool solve(){
    int head{0};
    int tail{N-1};
    int cur;
    int ret[2] = {0, 0};

    for (int i{0}; i<N; ++i){
        if (S[head] > S[tail]){
            cur = head;
            ++head;
        }else if(S[head] == S[tail]){
            if (S[head+1] > S[tail-1]){
                cur = head;
                ++head;
            }else{
                cur = tail;
                --tail;
            }
        }else{
            cur = tail;
            --tail;
        }
        ret[i%2] += S[cur];
    }

    return (ret[1]>ret[0]);
}

int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    std::cin >> T;
    while(--T){
        std::cin >> N;
        S.resize(N);
        for (int i{0}; i<N; ++i) std::cin >> S[i];
        if (solve()) std::cout << "All for one\n";
        else std::cout << "One for all\n";
    }

    return 0;
}