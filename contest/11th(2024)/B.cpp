#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>

int N, K;
std::vector<int> col(1, 0);

int fun(int k){
    int tmp;
    std::set<int> p;
    for (int j{0}; j<k; ++j){
        std::cin >> tmp;
        p.insert(tmp);
    }
    std::vector<int> vec;
    vec.assign(p.begin(), p.end());
    std::sort(vec.begin(), vec.end());

    int o{1};
    int color{0};
    for (int i{0}; i<p.size(); ++i){
        color += vec[i]*o;
        o *= 10;
    }
    return color;
}

int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    std::cin >> N;
    
    for (int i{0}; i<N; ++i){
        std::cin >> K;
        int tmp = fun(K);
        if (std::find(col.begin(), col.end(), tmp) == col.end()){
            col.push_back(tmp);
        }
    }
    
    std::cout << col.size()-1;

    return 0;
}