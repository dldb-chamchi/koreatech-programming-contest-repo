#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>

int N;
int M;
std::vector<std::string> problem; //문제 제목
bool large[101];
std::vector<int> nIdx;

int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    std::cin >> N;
    std::cin.ignore();
    for(int i{0}; i<N; ++i){
        std::string input = "";
        std::string title = "";
        std::getline(std::cin, input);

        if (input[input.size()-1] == ')'){
            if (input[input.size()-2] == 'e'){
                large[i] = true;
            }
            for (int j{0}; j<input.size()-8; ++j){
                title += input[j];
            }
        }else{
            for (int j{0}; j<input.size(); ++j){
                title += input[j];
            }
        }
        problem.push_back(title);
        // std::cout << "===: " << title << '\n';
    } 

    std::cin >> M;
    std::vector<int> solve(M);
    int tmpp;
    for (int i{0}; i<M; ++i){
        std::cin >> tmpp;
        solve[i] = tmpp-1;
    }

    for (auto n: solve){
        
        if (large[n]){//풀은 문제가 라지면
            std::string search = problem[n];
            problem[n] = "";

            //int sIdx = std::find(problem.begin(), problem.end(), search);
            //small 인덱스 찾기
            int sIdx{0};
            for (int i{0}; i<N; ++i){
                if (search==problem[i]){
                    sIdx = i;
                    break;
                }
            }

            
            //small 인덱스를 안풀었으면
            if (std::find(solve.begin(), solve.end(), sIdx)==solve.end()){
                nIdx.push_back(sIdx);
            }
        }
    }

    std::sort(nIdx.begin(), nIdx.end());
    std::cout << nIdx.size() << '\n';
    if (nIdx.size()!=0) for (auto i: nIdx) std::cout << i+1 << ' ';
    

    return 0;
}