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
    int ret[2] = {0, 0};

    for (int i{0}; i<N; ++i){
        int cur = -1;
        int deep{1};
        if (S[head]!=S[tail]){
            if (S[head]>S[tail])
                cur = head++;
            else cur = tail--;
        }else{
            while (deep<=(tail-head+1)/2){
                if (S[head+deep]==S[tail-deep]){
                    ++deep;
                    continue;
                }
                if (S[head+deep]>S[tail-deep]){
                    cur = tail--;
                    break;
                }else{
                    cur = head++;
                    break;
                }
            }
            if (cur == -1) cur = head--;
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
    while(T--){
        std::cin >> N;
        S.resize(N+1);
        for (int i{0}; i<N; ++i) std::cin >> S[i];

        if (solve()) std::cout << "All for one\n";
        else std::cout << "One for all\n";
    }

    return 0;
}