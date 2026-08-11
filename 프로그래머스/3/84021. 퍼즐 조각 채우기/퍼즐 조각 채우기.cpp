#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;

int n;
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

// 1. 좌표 정규화 함수: 가장 좌상단 좌표를 (0,0)으로 이동 후 정렬
vector<pii> normalize(vector<pii>& piece) {
    int min_r = 50, min_c = 50;
    for (const auto& p : piece) {
        min_r = min(min_r, p.first);
        min_c = min(min_c, p.second);
    }
    
    vector<pii> norm_piece;
    for (const auto& p : piece) {
        norm_piece.push_back({p.first - min_r, p.second - min_c});
    }
    
    // 좌표 정렬 (x 기준 오름차순, y 기준 오름차순)
    sort(norm_piece.begin(), norm_piece.end());
    return norm_piece;
}

// 2. 90도 시계 방향 회전 함수
vector<pii> rotate(vector<pii>& piece) {
    vector<pii> rotated;
    // (r, c) -> (c, -r)로 변환 후 정규화
    for (const auto& p : piece) {
        rotated.push_back({p.second, -p.first});
    }
    return normalize(rotated);
}

// 3. BFS를 이용해 연결된 조각/빈공간 추출
vector<vector<pii>> get_pieces(vector<vector<int>>& board, int target_val) {
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    vector<vector<pii>> pieces;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == target_val && !visited[i][j]) {
                queue<pii> q;
                vector<pii> piece;

                q.push({i, j});
                visited[i][j] = true;
                piece.push_back({i, j});

                while (!q.empty()) {
                    auto [r, c] = q.front();
                    q.pop();

                    for (int d = 0; d < 4; d++) {
                        int nr = r + dr[d];
                        int nc = c + dc[d];

                        if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                            if (!visited[nr][nc] && board[nr][nc] == target_val) {
                                visited[nr][nc] = true;
                                q.push({nr, nc});
                                piece.push_back({nr, nc});
                            }
                        }
                    }
                }
                // 추출한 좌표 집합을 정규화하여 저장
                pieces.push_back(normalize(piece));
            }
        }
    }
    return pieces;
}

int solution(vector<vector<int>> game_board, vector<vector<int>> table) {
    n = game_board.size();

    // 빈 공간(0)과 퍼즐 조각(1) 추출
    vector<vector<pii>> spaces = get_pieces(game_board, 0);
    vector<vector<pii>> blocks = get_pieces(table, 1);

    vector<bool> used(blocks.size(), false);
    int answer = 0;

    // 빈 공간마다 들어갈 수 있는 퍼즐 조각 비교
    for (const auto& space : spaces) {
        for (size_t i = 0; i < blocks.size(); i++) {
            // 이미 사용했거나 칸 수가 다르면 비교하지 않음
            if (used[i] || space.size() != blocks[i].size()) continue;

            vector<pii> curr_block = blocks[i];
            bool matched = false;

            // 0도, 90도, 180도, 270도 회전 시도
            for (int r = 0; r < 4; r++) {
                if (space == curr_block) {
                    answer += space.size();
                    used[i] = true;
                    matched = true;
                    break;
                }
                curr_block = rotate(curr_block);
            }

            if (matched) break; // 일치하는 조각을 찾았으면 다음 빈 공간으로
        }
    }

    return answer;
}