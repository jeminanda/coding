#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int m) {
    int maximumdivisor = 0;
    int minimum = 0;
    //최대 공약수
    for(int i = 1; i < n+1; i++)
    {
        if(n%i==0 && m%i ==0)
            maximumdivisor = i;
    }
    for(int i = 1; i*n<= n * m; i++)
    {
        if((i* n) % m == 0)
        {
            minimum = i * n;
            break;
        }
    }
    
    return {maximumdivisor,minimum};
}