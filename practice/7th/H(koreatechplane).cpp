#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>

//1171 7회 경시대회, H, KoreaTech 세계 일주를 꿈꾸다!

int fuel[355000];
int spendFuel[355000];
int total[355000];
int dp[355000];

int T, C;
bool first{false}, flag{false};
//양수 첫번째 , 마이너스 바로 뒤

void find(){
    for(int i{0}; i<C; ++i){
        if(total[i] < 0){
            flag = true;
        }
        else if(!first){
            solve(i);
            first = true;
        }
        else if(flag){
            solve(i);
            flag = false;
        }
    }
}

void solve(int idx){
    for(int i{idx}; i<C; ++i){
        fuel[idx]
    }
}

int main(){

    std::cin >> T;
    std::cin >> C;
    
    for(int t{0}; t<T; ++t){
        for(int c{0}; c<C; ++c){
            std::cin >> fuel[c];
        }
        for(int c{0}; c<C; ++c){
            std::cin >> spendFuel[c];
        }
        for(int i{0}; i<C; ++i){
            total[i] = fuel[i] - spendFuel[i];
        }
        for(int j{0}; j<C; ++j){
            fuel[j] = 0;
            spendFuel[j] = 0;
        }
        solve();
    }

    return 0;
}