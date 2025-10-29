#include <iostream>
#include <vector>
#include <queue>

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

    if(N==1){
        if(W[0]<=P) solution=1;
    }
    else if(N==2){
        if(W[0]<=P && W[1]<=P){
            if(W[0]+W[1]<=P)    solution=1;
            else                solution=2;
        }
        else{
            solution=2;
        }
    }
    else if(N==3){
        if(W[0]>P && W[1]>P && W[2]>P){ //셋다 커
            solution=3;
        }
        else if(W[0]<=P && W[1]<=P && W[2]<=P){ //셋다 작아
            if(W[0]+W[1] <= P){
                solution=2;
            }
            else if(W[0]+W[2] <=P){
                solution=2;
            }
            else if(W[1]+W[2] <=P){
                solution=2;
            }
            else{
                solution=3;
            }
        }
        else if((W[0]>P && W[1]>P && W[2]<=P) || (W[2]>P && W[1]>P && W[0]<=P) || (W[0]>P && W[2]>P && W[1]<=P)){  //하나만 커
            if(W[0]<P){
                if(W[1]+W[2]>P){
                    solution=3;
                }
                else solution=2;
            }
            else if(W[1]<P){
                if(W[0]+W[2]>P){
                    solution=3;
                }
                else solution=2;
            }
            else if(W[2]<P){
                if(W[0]+W[1]>P){
                    solution=3;
                }
                else solution=2;
            }
        }
        else{   //두개가 커
            solution=3;
        }
    }

    std::cout << solution;

    return 0;
}