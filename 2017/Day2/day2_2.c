#include<stdio.h>
#include<stdlib.h>
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
    int* line = malloc(n*sizeof(int));
    int num1;
    int num2;
    do {
        for (int i = 0; i < n; i++) {
            fscanf(file_ptr, "%d", &line[i]);
        }
        for (int i = 0; i < n-1; i++) {
            for (int j = i+1; j < n; j++) {
                if (line[i] % line[j] == 0) {
                    checksum += line[i] / line[j];
                    break;
                } else if (line[j] % line[i] == 0) {
                    checksum += line[j] / line[i];
                    break;
                }
            }
        }
    } while (getc(file_ptr) != EOF); 

    printf("\n%d",checksum);

    fclose(file_ptr);
    return 0;
}