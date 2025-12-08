#include<stdio.h>

int main() {

    FILE *file_ptr1;
    FILE *file_ptr2;

    file_ptr1 = fopen("day1.txt", "r");
    file_ptr2 = fopen("day1.txt", "r");

    if (NULL == file_ptr1 || NULL == file_ptr2) {
        printf("file can't be opened \n");
          return 0;
    }

    fseek(file_ptr2, 0L, SEEK_END);
    int n = ftell(file_ptr2);

    //printf("File Size: %d\n", n);

    fseek(file_ptr2, n / 2, SEEK_SET);

    int total = 0;

    int dig1;
    int dig2;

    for (int i = 0; i < n; i++) {
        dig1 = fgetc(file_ptr1);
        dig2 = fgetc(file_ptr2);
        //printf("%c  %c\n", dig1, dig2);

        if (dig1 == EOF) {
            fseek(file_ptr1, 0L, SEEK_SET);
            dig1 = fgetc(file_ptr1);
        }
        if (dig2 == EOF) {
            fseek(file_ptr2, 0L, SEEK_SET);
            dig2 = fgetc(file_ptr2);
        }

        if (dig1 == dig2) {
            total += dig1 - 48;
        }
    }

    printf("%d", total);

    fclose(file_ptr1);
    fclose(file_ptr2);
    return 0;
}