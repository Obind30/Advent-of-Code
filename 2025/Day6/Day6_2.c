#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define ROWCOUNT 4

typedef struct File_List {
    FILE* fptr;
    struct File_List* next;
} File_List;

File_List* Node_Construct(long int pos) {
    File_List* node = malloc(sizeof(File_List));
    if (node == NULL) {return NULL;}
    node -> fptr = fopen("Day6.txt", "r");
    if (node->fptr == NULL) {return NULL;}
    fseek(node->fptr, pos, SEEK_SET);
    node -> next = NULL;
    return node;
}

void List_Destruct(File_List* head) {
    while (head != NULL) {
		File_List* p = head -> next;
        fclose(head->fptr);
		free(head);
		head = p;
	}
}

int main() {
    FILE *file_ptr;

    file_ptr = fopen("Day6.txt", "r");

    if (file_ptr == NULL) {
        printf("file can't be opened \n");
        return 0;
    }

    File_List* fptrList = NULL;
    File_List* node = NULL;

    unsigned long long int grandTotal = 0;

    char currChar = '\0';
    int lineLength = 0;
    while (currChar != '\n') {
        currChar = fgetc(file_ptr);
        lineLength++;
    }
    //printf("%d\n", lineLength);
    for (int i=ROWCOUNT-1; i>=0; i--) {
        node = Node_Construct(i*(lineLength+1));
        printf("%d\n", i*lineLength);
        node->next = fptrList;
        fptrList = node;
    }
    fseek(file_ptr, ROWCOUNT*(lineLength+1), SEEK_SET);

    char operator = '\n';
    unsigned long long int colSum = 0;
    for (int i=0; i<lineLength; i++){
        node = fptrList;

        char operLine = fgetc(file_ptr);
        if (operLine != ' ') {
            printf("%llu\n", colSum);
            operator = operLine;
            grandTotal += colSum;
            colSum = 0;
        }

        int colNum = 0;
        while (node) {
            int num = fgetc(node->fptr)-48;
            if (num > 0) {
                colNum *= 10;
                colNum += num;
            }
            node = node->next;
        }

        if (operator == '+' || (operator == '*' && colSum == 0)) {
            colSum += colNum;
            printf("+%d->", colNum);
        } else if (operator == '*' && colNum > 0) {
            colSum *= colNum;
            printf("*%d->", colNum);
        }
    }
    printf("%llu\n", colSum);
    grandTotal += colSum;

    printf("The grand total is: %llu\n", grandTotal);
    List_Destruct(fptrList);
    fclose(file_ptr);
    return 1;
}