#include <string>
#include <vector>
#include <sstream>

using namespace std;

int solution(string s) {
    int answer = 0;
    stringstream ss(s);
    string token;
    vector<int> stack;
    while (ss >> token)
    {
        if (token == "Z")
        {
            if(!stack.empty())
            {
                stack.pop_back();
            }
        }
         else
            {
                stack.push_back(stoi(token));
            }
    }
    for(int num : stack)
    {
        answer += num;
    }
    return answer;
}