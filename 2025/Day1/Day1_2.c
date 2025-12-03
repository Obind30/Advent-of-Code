#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX_LINE_LENGTH 10

int main() {

    FILE *file_ptr;

    file_ptr = fopen("Day1.txt", "r");

    if (NULL == file_ptr) {
        printf("file can't be opened \n");
        return 0;
    }

    int wheelSize = 100;
    int pointerLocation = 50;
    char line[MAX_LINE_LENGTH];
    char substring [MAX_LINE_LENGTH];
    int moveCount;
    int score = 0;

    while (fgets(line, MAX_LINE_LENGTH, file_ptr)) {
        strncpy(substring, line+1, strlen(line)-2);
        substring[strlen(line)-2] = '\0';
        moveCount = strtol(substring, NULL, 10);
        if (line[0] == 'L') {
            score += (((wheelSize-pointerLocation)%wheelSize)+moveCount)/wheelSize;
            pointerLocation = (pointerLocation+(wheelSize-(moveCount%wheelSize)))%wheelSize;
        } else if (line[0] == 'R') {
            score += (moveCount+pointerLocation)/wheelSize;
            pointerLocation = (pointerLocation+moveCount)%wheelSize;
        }
    }
    printf("The password is: %d\n", score);

    fclose(file_ptr);
    return 1;
}