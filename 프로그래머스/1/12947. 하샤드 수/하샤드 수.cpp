#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    int sum = 0;
    int temp = x;
    while(temp)
    {
        sum = sum + temp%10;
        temp = temp/10;
    }
    if(!(x%sum))
        return true;
    else
        return false;
}