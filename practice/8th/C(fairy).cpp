//C
#include <iostream>
#include <vector>

int T, W, H;
int map[30][30];

// void testMapPrint(){
//     std::cout << "------map-----\n";
//     for(int i{0}; i<H; ++i){
//         for(int j{0}; j<W; ++j){
//             std::cout << map[i][j] << ' ';
//         }
//         std::cout << '\n';
//     }
// }

void solve(){

}

int main() {
    std::cin >> T;
    for(int t{0}; t<T; ++t){
        std::cin >> W >> H;
        for(int i{0}; i<H; ++i){
            for(int j{0}; j<W; ++j){
                std::cin >> map[i][j];
            }
        }

        solve();
    }

    return 0;
}