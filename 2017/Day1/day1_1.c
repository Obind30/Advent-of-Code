#include<stdio.h>

int main() {

    FILE *file_ptr;

    file_ptr = fopen("day1.txt", "r");

    if (NULL == file_ptr) {
        printf("file can't be opened \n");
          return 0;
    }

    int total = 0;

    int first;

    int curr;
    int last;

    first = fgetc(file_ptr);
    last = first;

    while ((curr = fgetc(file_ptr)) != EOF) {
        if (curr == last) {
            total += curr - 48;
        }
        last = curr;
    }

    if (last == first) {
        total += first - 48;
    }

    printf("%d", total);

    fclose(file_ptr);
    return 0;
}