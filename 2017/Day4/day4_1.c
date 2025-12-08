#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int main() {
    FILE* fptr;
    fptr = fopen("input.txt", "r");
    if (fptr == NULL) {return EXIT_FAILURE;}
    char* line = NULL;
    do {
        fgets(line, 10000, fptr);

    } while (line != NULL);

    return EXIT_SUCCESS;
}