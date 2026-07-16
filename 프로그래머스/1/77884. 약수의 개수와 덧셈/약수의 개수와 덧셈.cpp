#include <string>
#include <vector>

using namespace std;

int solution(int left, int right) {
    int answer = 0;
    for(int i = left; i < right+1; i++)
    {
        int factor = 0;
        for(int j = 1; j < i+1; j++)
        {
            if((i % j) == 0)
                factor++;
        }
        if ((factor%2)==0)
            answer = answer + i;
        else
            answer = answer - i;
    }
    return answer;
}