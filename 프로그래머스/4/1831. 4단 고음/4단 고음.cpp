#include <cmath>

int answer = 0;

void dfs(int n, int plus) {
    // 기저 사례: n이 3이고, 짝이 맞는 '+'가 정확히 2개 남았을 때
    if (n == 3) {
        if (plus == 2) answer++;
        return;
    }
    
    // 가능 범위 이탈 조건
    // 남아있는 3의 거듭제곱보다 n이 작아지면 올바른 성립 불가
    if (n < 3 || log(n) / log(3) * 2 < plus) return;

    // 1. 3으로 나누는 경우 ('*' 연산 적용)
    if (n % 3 == 0 && plus >= 2) {
        dfs(n / 3, plus - 2);
    }

    // 2. 1을 빼는 경우 ('+' 연산 적용)
    dfs(n - 1, plus + 1);
}

int solution(int n) {
    answer = 0;
    dfs(n , 0);
    return answer;
}