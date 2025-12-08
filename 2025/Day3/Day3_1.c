#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main() {
    FILE *file_ptr;
    FILE *tens_ptr;

    file_ptr = fopen("Day3.txt", "r");
    tens_ptr = fopen("Day3.txt", "r");

    if (file_ptr == NULL || tens_ptr == NULL) {
        printf("file can't be opened \n");
        return 0;
    }

    int lineLength = 0;
    
    char currentChar = '\0';
    int currentDigit;

    int tens = 0;
    int ones = 0;

    int joltage = 0;

    while (currentChar != '\n') {
        currentChar = fgetc(file_ptr);
        lineLength++;
    }
    lineLength -= 1;
    fseek(file_ptr, 0, SEEK_SET);

    currentChar = fgetc(file_ptr);
    while (currentChar != EOF) {
        for (int pos = 1; pos < lineLength; pos++) {
            currentDigit = strtol(&currentChar, NULL, 10);
            if (currentDigit > tens) {
                tens = currentDigit;
                fseek(tens_ptr, ftell(file_ptr)-sizeof(char), SEEK_SET);
            }
            currentChar = fgetc(file_ptr);
        }
        fseek(file_ptr, ftell(tens_ptr)+sizeof(char), SEEK_SET);
        currentChar = '\0';
        while (currentChar != '\n') {
            currentChar = fgetc(file_ptr);
            currentDigit = strtol(&currentChar, NULL, 10);
            if (currentDigit > ones) {
                ones = currentDigit;
            }
        }
        joltage += tens*10+ones;
        printf("%d\n", tens*10+ones);
        tens = 0;
        ones = 0;
        currentChar = fgetc(file_ptr);
    }
    printf("The total joltage is %d\n", joltage);
    fclose(file_ptr);
    fclose(tens_ptr);
    return 1;
}