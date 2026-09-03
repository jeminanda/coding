#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int** sizes, size_t sizes_rows, size_t sizes_cols) {
    int max_w = 0;
    int max_h = 0;

    for (size_t i = 0; i < sizes_rows; i++) {
        int w = sizes[i][0] > sizes[i][1] ? sizes[i][0] : sizes[i][1];
        int h = sizes[i][0] < sizes[i][1] ? sizes[i][0] : sizes[i][1];

        if (w > max_w) max_w = w;
        if (h > max_h) max_h = h;
    }

    return max_w * max_h;
}