#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iomanip>

using namespace std;

// "HH:MM" -> 분(int) 변환 함수
int toMinutes(const string& timeStr) {
    stringstream ss(timeStr);
    string hourStr, minStr;
    getline(ss, hourStr, ':');
    getline(ss, minStr, ':');
    return stoi(hourStr) * 60 + stoi(minStr);
}

// 분(int) -> "HH:MM" 변환 함수
string toTimeString(int totalMin) {
    int h = totalMin / 60;
    int m = totalMin % 60;
    
    stringstream ss;
    ss << setfill('0') << setw(2) << h << ":" 
       << setfill('0') << setw(2) << m;
    return ss.str();
}

string solution(int n, int t, int m, vector<string> timetable) {
    // 1. 크루들 도착 시각(분 단위) 변환 및 정렬
    vector<int> crewTimes;
    for (const string& time : timetable) {
        crewTimes.push_back(toMinutes(time));
    }
    sort(crewTimes.begin(), crewTimes.end());

    int crewIdx = 0;
    int shuttleTime = 540; // 첫 셔틀: 09:00 (9 * 60 = 540분)
    int lastBoardedTime = 0;
    int boardedCount = 0;

    // 2. n 번의 셔틀 운행 시뮬레이션
    for (int i = 0; i < n; i++) {
        boardedCount = 0;
        
        // 해당 셔틀 시간에 탈 수 있는 크루들을 정원(m)까지 기차에 탑승 처리
        while (crewIdx < crewTimes.size() && crewTimes[crewIdx] <= shuttleTime && boardedCount < m) {
            lastBoardedTime = crewTimes[crewIdx]; // 가장 최근에 탄 크루 시간 기록
            crewIdx++;
            boardedCount++;
        }
        
        // 마지막 셔틀이 아니라면 다음 셔틀 시각 계산
        if (i < n - 1) {
            shuttleTime += t;
        }
    }

    // 3. 콘의 최적 도착 시간 계산
    int conTime = 0;
    if (boardedCount < m) {
        // 마지막 셔틀에 자리가 남아있다면 셔틀도착 시각에 오면 됨
        conTime = shuttleTime;
    } else {
        // 마지막 셔틀이 만석이면, 맨 마지막으로 탄 크루보다 1분 일찍 와야 함
        conTime = lastBoardedTime - 1;
    }

    return toTimeString(conTime);
}