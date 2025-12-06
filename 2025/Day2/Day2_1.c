#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>
#include<math.h>
#define MAX_LINE_LENGTH 10

long long int Pow10(long long int val) {
    int ret = 1;
    for (int i = 0; i < val; i++) {
        ret *= 10;
    }
    return ret;
}

int numDigits(long long int val) {
    int digits = 0;
    while (val > 0) {
        val -= val % 10;
        val /= 10;
        digits += 1;
    }
    return digits;
}

struct Boundary {
    long long int limit;
    int digits;
};

int main() {
    FILE *file_ptr;

    file_ptr = fopen("Day2.txt", "r");

    if (NULL == file_ptr) {
        printf("file can't be opened \n");
        return 0;
    }

    char currentChar;
    bool low = true;
    struct Boundary rangeLow;
    struct Boundary rangeHigh;
    rangeLow.limit = 0;
    rangeLow.digits = 0;
    rangeHigh.limit = 0;
    rangeHigh.digits = 0;

    unsigned long long int invalidIDS = 0;
    while (true) {
        currentChar = fgetc(file_ptr);
        if (currentChar == ',' || currentChar == EOF) {

            struct Boundary checking;
            checking.digits = rangeLow.digits + rangeLow.digits%2;
            long long int smallNum = Pow10((checking.digits/2)-1);
            checking.limit = smallNum + smallNum*Pow10(checking.digits/2);
            while (checking.limit <= rangeHigh.limit) {
                if (checking.limit >= rangeLow.limit) {
                    printf("%lld \n", checking.limit);
                    invalidIDS += checking.limit;
                }
                smallNum += 1;
                checking.limit = smallNum + smallNum*Pow10(numDigits(smallNum));
            }
            
            low = true;
            rangeLow.limit = 0;
            rangeLow.digits = 0;
            rangeHigh.limit = 0;
            rangeHigh.digits = 0;     
            if (currentChar == EOF) {break;}  
        } else if (currentChar == '-') {
            low = !(low);
        } else {
            if (low) {
                rangeLow.digits += 1;
                rangeLow.limit *= 10;
                rangeLow.limit += strtol(&currentChar, NULL, 10);
            } else {
                rangeHigh.digits += 1;
                rangeHigh.limit *= 10;
                rangeHigh.limit += strtol(&currentChar, NULL, 10);
            }
        }
    }
    printf("The score is: %llu", invalidIDS);

    fclose(file_ptr);
    return 1;
}