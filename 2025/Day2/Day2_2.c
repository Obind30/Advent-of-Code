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

bool checkInvalid(long long int number, int digits) {
    if (digits == 1) {return false;}
    for (int div = 1; div <= digits/2; div++) {
        // digits is number of digits that keys are generating
        // div is number of digits in sub pattern
        if (digits%div == 0) {
            long long int pattern = Pow10(div-1);
            long long int checking = pattern;
            for (int i = 1; i<digits/div; i++) {
                checking *= Pow10(div);
                checking += pattern;
            }
            while (checking <= number) {                
                if (checking == number) {
                    return true;
                }
                pattern += 1;
                checking = pattern;
                for (int i = 1; i<digits/div; i++) {
                    checking *= Pow10(div);
                    checking += pattern;
                }
            }
        }
    }
    return false;
}

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
            for (int digits = rangeLow.digits; digits <= rangeHigh.digits; digits++) {
                for (int div = 1; div <= digits/2; div++) {
                    // digits is number of digits that keys are generating
                    // div is number of digits in sub pattern
                    if (digits%div == 0) {
                        long long int pattern = Pow10(div-1);
                        long long int checking = pattern;
                        for (int i = 1; i<digits/div; i++) {
                            checking *= Pow10(div);
                            checking += pattern;
                        }
                        while (checking <= rangeHigh.limit && numDigits(checking) == digits) {   
                            if (checking >= rangeLow.limit && !(checkInvalid(pattern, div))) {
                                printf("%lld    %lld \n", pattern, checking);
                                invalidIDS += checking;
                            }
                            pattern += 1;
                            checking = pattern;
                            for (int i = 1; i<digits/div; i++) {
                                checking *= Pow10(div);
                                checking += pattern;
                            }
                        }
                    }
                }
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