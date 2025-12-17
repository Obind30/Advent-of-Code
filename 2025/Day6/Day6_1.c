#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct Col {
    int value;
    struct Col* next;
} Collumn;

typedef struct List {
    Collumn* col;
    char operator;
    struct List* next;
} List;

Collumn* Collumn_Construct(int value) {
    Collumn* node = malloc(sizeof(Collumn));
    if (node == NULL) {return NULL;}
    node -> value = value;
    node -> next = NULL;
    return node;
}

List* Node_Construct(int initVal) {
    List* node = malloc(sizeof(List));
    if (node == NULL) {return NULL;}
    node -> col = Collumn_Construct(initVal);
    node -> next = NULL;
    return node;
}

void Collumn_Descruct(Collumn* head) {
    while (head != NULL) {
		Collumn* p = head -> next;
		free(head);
		head = p;
	}
}

void List_Destruct(List* head) {
    while (head != NULL) {
		List* p = head -> next;
        Collumn_Descruct(head->col);
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

    int lineLength = 0;
    List* dataList = NULL;

    unsigned long long int grandTotal = 0;

    char whitespace;
    int value;
    List* node = dataList;
    while (whitespace != '\n') {
        fscanf(file_ptr, "%d", &value);
        whitespace = fgetc(file_ptr);
        List* newNode = Node_Construct(value);
        if (dataList) {
            node->next = newNode;
            node = node->next;
        } else {
            dataList = newNode;
            node = dataList;
        }

        lineLength++;
    }

    for (int j = 0; j<3; j++) {
        node = dataList;
        for (int i=0; i<lineLength; i++) {
            fscanf(file_ptr, "%d", &value);
            Collumn* new = Collumn_Construct(value);
            new->next = node->col;
            node->col = new;

            node = node->next;
        } 
    }
    char operator;
    node = dataList;
    while (node) {
        operator = ' ';
        while (operator == ' ' || operator == '\n') {
            operator = fgetc(file_ptr);
        }
        node->operator = operator;
        node = node->next;
    } 
    node = dataList;
    while (node) {
        Collumn* colNode = node->col;
        char oper = node->operator;
        unsigned long long int sum = 0;
        while (colNode) {
            if (oper == '+') {
                sum += colNode->value;
                printf("+%d -> ", colNode->value);
            } else if (oper == '*') {
                sum *= colNode->value;
                printf("*%d -> ", colNode->value);
                if (sum == 0) {sum += colNode->value;}
            }
            colNode = colNode -> next;
        }
        printf("%llu\n", sum);
        grandTotal += sum;
        node = node->next;
    }



    printf("The grand total is: %llu\n", grandTotal);
    List_Destruct(dataList);
    fclose(file_ptr);
    return 1;
}