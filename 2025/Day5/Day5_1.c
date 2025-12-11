#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX_LINE_LENGTH 35

typedef struct List {
    unsigned long long int value;
    struct List* next;
} List;

List* Node_Construct(unsigned long long int val) {
    List* node = malloc(sizeof(List));
    if (node == NULL) {return NULL;}
    node -> value = val;
    node -> next = NULL;
    return node;
}

void List_Destruct(List* head) {
    while (head != NULL) {
		List* p = head -> next;
		free(head);
		head = p;
	}
}

List* List_Delete(List* head, List* val) {
    List* q = head;
    if (head == val) {
        head = head -> next;
		free(q);
		return head;
    }

    while((q != NULL) && ((q -> next) != val)) {
		q = q -> next; 
	}
	if (q != NULL) {
		q -> next = val -> next;
		free(val);
	}
	return head;
}

List* List_Insert(List* head, unsigned long long int val) {
    List* node = Node_Construct(val);
    node -> next = head;
    return node;
}

void Print_List(List * head) {
    List * p = head;
    while (p) {
        printf("%d->", p -> value);
        p = p -> next;
    }
    printf("\n");
}

int main() {
    FILE *file_ptr;

    file_ptr = fopen("Day5.txt", "r");

    if (file_ptr == NULL) {
        printf("file can't be opened \n");
        return 0;
    }

    char line[MAX_LINE_LENGTH];

    while (strcmp(line, "\n")) {
        fgets(line, MAX_LINE_LENGTH, file_ptr);
    }


    List* IngredientIDS = NULL;
    unsigned long long int ID;

    while (fscanf(file_ptr, "%llu\n", &ID) > 0) {
        IngredientIDS = List_Insert(IngredientIDS, ID);
    }


    fseek(file_ptr, 0, SEEK_SET);

    unsigned long long int lowLim;
    unsigned long long int highLim;
    int fresh = 0;
    
    while (fscanf(file_ptr, "%llu-%llu\n", &lowLim, &highLim) > 1) {
        List* node = IngredientIDS;
        while (node) {
            if (node->value >= lowLim && node->value <= highLim) {
                IngredientIDS = List_Delete(IngredientIDS, node);
                fresh++;
            }
            node = node -> next;
        }
    }

    printf("There are %d fresh ingredients\n", fresh);
    List_Destruct(IngredientIDS);
    fclose(file_ptr);
    return 1;
}