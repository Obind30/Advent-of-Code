#include <math.h>
#include <stdio.h>
#define NUM 347991

int main() {
    int level = ceil(sqrt(NUM));
    level += 1-(level%2);

    int corners = 0;
    int min_corner_dist = NUM+1;
    for (int i=0; i<4; i++) {
        corners = level*level - i*(level-1);
        if (corners >= NUM && corners - NUM < min_corner_dist) {
            min_corner_dist = corners - NUM;
        } else if (NUM - corners < min_corner_dist) {
            min_corner_dist = NUM - corners;
        }
    }

    printf("%d", level-1-min_corner_dist);
    return 1;
}