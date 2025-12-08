#include<stdio.h>
#include<math.h>

int main() {
  
    FILE *file_ptr;
    file_ptr = fopen("day2.txt", "r");

    if (NULL == file_ptr) {
        printf("File can't be opened \n");
    }

    int n = 0;
    char last = 0;
    char character;
    fscanf(file_ptr, "%c", &character);
    while (character != '\n') {
        if ((character == 9 || character == ' ') && character != last) {
            n++;
        }
        last = character;
        fscanf(file_ptr, "%c", &character);
    }
    n++;

    printf("%d\n\n", n);
    fseek(file_ptr, 0, SEEK_SET);
    
    int checksum = 0;
    int num;
    do {
        int min = 2147483647;
        int max = 0;
        for (int i = 0; i < n; i++) {
            fscanf(file_ptr, "%d", &num);
            if (num > max) {
                max = num;
            } 
            if (num < min) {
                min = num;
            }
        }
        checksum += max - min;
    } while (getc(file_ptr) != EOF); 

    printf("\n%d",checksum);

    fclose(file_ptr);
    return 0;
}