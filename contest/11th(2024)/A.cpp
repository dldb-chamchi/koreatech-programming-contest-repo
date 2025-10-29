#include <iostream>
#include <vector>
#include <queue>


int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    int N, A, B;

    std::cin >> N >> A >> B;
    int ret = N*A<B ? N*A:B;

    std::cout << ret;

    return 0;
}