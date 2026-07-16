#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board) {
    int answer = 0;
    vector<vector<int>> safearea = board;
    int n = board.size();
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(board[i][j] == 1)
            {
                for(int k = i-1; k < i + 2; k++)
                {
                    for(int l = j -1; l < j +2; l++)
                    {
                        if(k >= 0 && l >= 0 && k < n && l < n )
                        {
                            safearea[k][l] = 1;
                        }
                    }
                }
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(safearea[i][j] == 0)
                answer++;
        }
    }
    return answer;
}