#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

int N;
std::vector<int> W;
int P;

int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    int solution{0};
    std::cin >> N;  //물건 개수
    W.resize(N);
    for(int i{0}; i<N; ++i){
        std::cin >> W[i];
    }
    std::cin >> P;  //힘
    std::sort(W.begin(), W.end());

    // std::cout << "---------\n";
    // for(int i{0}; i<N; ++i){
    //     std::cout << W[i] << ' ';
    // }
    // std::cout << "\n---------\n";

    int left{N-1};  //인덱스임
    for(int r{0}; r<N; ++r){
        //std::cout << solution << ' ' << r << ' ' << left << '\n';
        if(r==left){
            solution+=1;
            break;
        }
        else if(left<r){
            break;
        }

        //std::cout << W[r] << ' ' << W[left] << '\n';

        if(W[r]+W[left] <= P){
            solution+=1;
            left-=1;
        }
        else{
            solution+=1;
            left-=1;
            r-=1;
        }
        
    }

    std::cout << solution;

    return 0;
}