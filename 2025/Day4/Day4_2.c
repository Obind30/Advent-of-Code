#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main() {
    FILE *file_ptr;

    file_ptr = fopen("Day4.txt", "r");

    if (file_ptr == NULL) {
        printf("file can't be opened \n");
        return 0;
    }

    int lineLength = 0;
    char currentChar;

    while (currentChar != '\n') {
        currentChar = fgetc(file_ptr);
        lineLength++;
    }
    lineLength -= 1;
    fseek(file_ptr, 0, SEEK_SET);

    int** grid = malloc(lineLength * sizeof(int*));
    for (int i = 0; i < lineLength; i++) {
        grid[i] = malloc(lineLength * sizeof(int));
    }

    for (int row = 0; row < lineLength; row++) {
        for (int col = 0; col < lineLength; col++) {
            currentChar = fgetc(file_ptr);
            if (currentChar == '@') {grid[row][col] = 1;}
            else {grid[row][col] = 0;}
        }
        currentChar = fgetc(file_ptr);
    }

    int offsets[8][2] = {
        {1,0},
        {1,1},
        {0,1},
        {-1,1},
        {-1,0},
        {-1,-1},
        {0,-1},
        {1,-1}
    };

    int removedRolls = 0;
    int availableRolls = 0;
    int adjacentRolls;
    int rowCheck;
    int colCheck;

    while (1) {
        for (int row = 0; row < lineLength; row++) {
            for (int col = 0; col < lineLength; col++) {
                if (grid[row][col] == 1) {
                    adjacentRolls = 0;
                    for (int i = 0; i < 8; i++) {
                        rowCheck = row+offsets[i][0];
                        colCheck = col+offsets[i][1];
                        if (rowCheck >= 0 && rowCheck < lineLength
                        && colCheck >= 0 && colCheck < lineLength
                        && grid[rowCheck][colCheck] == 1) {
                            adjacentRolls++;
                        }
                    }
                    if (adjacentRolls < 4) {
                        availableRolls++;
                        grid[row][col] = 0;
                    }
                }
            }
        }
        if (availableRolls == 0) {break;}
        removedRolls += availableRolls;
        availableRolls = 0;
    }

    printf("There are %d available rolls\n", removedRolls);

    for (int i = 0; i < lineLength; i++) {
        free(grid[i]);
    }
    free(grid);

    fclose(file_ptr);
    return 1;
}