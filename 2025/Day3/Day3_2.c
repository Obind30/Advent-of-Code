#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define BATTERY_NUM  12

typedef struct InfInt {
    int value;
    struct InfInt* next;
} InfInt;

InfInt* Node_Construct(int val) {
    InfInt* node = malloc(sizeof(node));
    if (node == NULL) {return NULL;}
    node -> value = val;
    node -> next = NULL;
    return node;
}

void List_Destruct(InfInt* head) {
    while (head != NULL) {
		InfInt* p = head -> next;
		free(head);
		head = p;
	}
}

InfInt* Digit_Insert(InfInt* head, int val) {
    InfInt* node = Node_Construct(val);
    node -> next = head;
    return node;
}

InfInt* Add_Lists(InfInt* List1, InfInt* List2) {
    InfInt* head = Node_Construct(0);
    InfInt* p = head;
    
    InfInt* p1 = List1;
    InfInt* p2 = List2;

    int carry = 0;
    int sum = 0;
    while (p1 != NULL || p2 != NULL || carry > 0) {

        if (p1 != NULL && p2 != NULL) {sum = p1 -> value + p2 -> value + carry;}
        else if (p1 != NULL) {sum = p1 -> value + carry;}
        else if (p2 != NULL) {sum = p2 -> value + carry;}
        else {sum = carry;}
        p -> value = sum%10;
        carry = sum/10;
        if ((p1 && p1 -> next != NULL) || (p2 && p2 -> next != NULL) || carry > 0) {
            p -> next = Node_Construct(0);
            p = p -> next;
        }
        if (p1 != NULL) {p1 = p1 -> next;}
        if (p2 != NULL) {p2 = p2 -> next;}
    }

    return head;
}

InfInt* List_Reverse(InfInt* head) {
	if (head == NULL) {return NULL;}
	
	InfInt* orighead = head;
	InfInt* revhead = NULL;
	InfInt* origsec = NULL;

	while(orighead != NULL) {
		origsec = orighead -> next;
		orighead -> next = revhead;
		revhead = orighead;
		orighead = origsec;
	}
	return revhead;
}

void Print_List(InfInt * head) {
    InfInt * p = head;
    while (p) {
        printf("%d", p -> value);
        p = p -> next;
    }
}

int main() {
    FILE *file_ptr;
    FILE *digi_ptr;

    file_ptr = fopen("Day3.txt", "r");
    digi_ptr = fopen("Day3.txt", "r");

    if (file_ptr == NULL || digi_ptr == NULL) {
        printf("file can't be opened \n");
        return 0;
    }

    int lineLength = 0;
    
    char currentChar = '\0';
    int currentDigit;
    int maxDigit;
    int maxDigPos = 0;

    InfInt* bankJoltage = NULL;

    InfInt* totalJoltage = NULL;

    while (currentChar != '\n') {
        currentChar = fgetc(file_ptr);
        lineLength++;
    }
    lineLength -= 1;
    fseek(file_ptr, 0, SEEK_SET);

    currentChar = fgetc(file_ptr);
    while (currentChar != EOF) {
        for (int i = BATTERY_NUM; i > 0; i--) {
            for (int pos = maxDigPos; pos < lineLength-i+1; pos++) {
                currentDigit = strtol(&currentChar, NULL, 10);
                if (currentDigit > maxDigit) {
                    maxDigit = currentDigit;
                    maxDigPos = pos+1;
                    fseek(digi_ptr, ftell(file_ptr)-sizeof(char), SEEK_SET);
                }
                currentChar = fgetc(file_ptr);
            }
            bankJoltage = Digit_Insert(bankJoltage, maxDigit);
            printf("%d", maxDigit);
            maxDigit = 0;
            fseek(file_ptr, ftell(digi_ptr)+sizeof(char), SEEK_SET);
            currentChar = fgetc(file_ptr);
        }
        // This is terrible, fix this
        // Navigate fptr to next line, for some reason +1 is only needed when maxDigPos does NOT equal the line length
        fseek(file_ptr, (1-(maxDigPos/lineLength))+lineLength-maxDigPos, SEEK_CUR);
        currentChar = fgetc(file_ptr);

        totalJoltage = Add_Lists(totalJoltage, bankJoltage);
        totalJoltage = List_Reverse(totalJoltage);
        printf("    ");
        Print_List(totalJoltage);
        totalJoltage = List_Reverse(totalJoltage);

        printf("    ");
        Print_List(List_Reverse(bankJoltage));

        List_Destruct(bankJoltage);
        bankJoltage = NULL;
        maxDigPos = 0;
        maxDigit = 0;
        printf("\n");
    }

    totalJoltage = List_Reverse(totalJoltage);
    printf("The total joltage is: ");
    Print_List(totalJoltage);
    printf("\n");

    List_Destruct(totalJoltage);
    List_Destruct(bankJoltage);
    fclose(file_ptr);
    fclose(digi_ptr);
    return 1;
}