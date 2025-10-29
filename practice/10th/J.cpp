#include <iostream>
#include <vector>
#include <cmath>
//10회 J

int E;
std::vector<std::vector<int>> F;
std::vector<std::vector<int>> L;
int date[100001];
std::vector<int> sums;

void testDatePrint(int maxDate){
    std::cout << "-----Date-----\n";
    for(int i{0}; i<=maxDate; ++i)
        std::cout << date[i] << ' ';
    std::cout << "\n----------\n";
}

void solve(int maxDate, int minDate){
    int sum{0}, idx{0};
    std::cout << maxDate << ' ' << minDate << '\n';
    for(int i{minDate}; i<=maxDate; ++i){
        for(int j{0}; j<F[i].size(); ++j){
            sum+=F[i][j];
        }
        for(int j{0}; j<L[i].size(); ++j){
            sum-=L[i][j];
        }
        date[i]=sum;
    }
    testDatePrint(maxDate);

    int back{minDate};
    for(int i{minDate+1}; i<=maxDate; ++i){
        if(date[back]!=date[i]){
            std::cout << back << ' ' << i << ' ' << date[back] << '\n';
            back=i;
        }
    }

}

int main(){

    int T;
    std::cin >> T;

    int f, l, tmp, maxDate{0}, minDate{1000000};
    for(int t{0}; t<T; ++t){
        std::cin >> E;
        F.resize(100001);
        L.resize(100001);
        for(int i{0}; i<E; ++i){
            std::cin >> f >> l >> tmp;
            
            F[f].push_back(tmp);
            L[l].push_back(tmp);
            if(maxDate<l)   maxDate=l;
            if(minDate>f)   minDate=f;
        }
        std::cout << "zz";

        solve(maxDate, minDate);
        std::cout << "\n---------------------\n";
        F.clear();
        L.clear();
        std::fill(date, date+maxDate, 0);
    }

    return 0;
}