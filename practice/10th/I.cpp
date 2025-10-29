#include <iostream>
#include <vector>

int student, cornerNum;
std::vector<int> corner;

int solve(){
    int time{0};
    int solution;
    int stayStudent{student};

    while (stayStudent==0){
        ++time;
        
    }
    

    return solution;
}

int main(){
    int T;
    std::cin >> T;
    for(int t{0}; t<T; ++t){
        std::cin >> student >> cornerNum;
        corner.resize(cornerNum);
        for(int i{0}; i<cornerNum; ++i)
            std::cin >> corner[i];
        
        solve();
    }

    return 0;
}