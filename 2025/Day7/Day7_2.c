#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define ROWCOUNT 4

typedef struct List {
    int col;
    unsigned long long int timelines;
    struct List* next;
} List;

List* Node_Construct(int col, unsigned long long int timelines) {
    List* node = malloc(sizeof(List));
    if (node == NULL) {return NULL;}
    node -> col = col;
    node -> timelines = timelines;
    node -> next = NULL;
    return node;
}

unsigned long long int Print_List(List* head) {
    List* p = head;
    unsigned long long int sum = 0;
    while(p) {
        printf("%llu->", p->timelines);
        sum += p->timelines;
        p = p->next;
    }
    printf("\n");
    return sum;
}

void List_Destruct(List* head) {
    while (head != NULL) {
		List* p = head -> next;
		free(head);
		head = p;
	}
}

int main() {
    FILE *file_ptr;
    file_ptr = fopen("Day7.txt", "r");
    if (file_ptr == NULL) {
        printf("file can't be opened \n");
        return 0;
    }

    List* beams = NULL;

    char currentChar = '\0';
    int inpWidth = 0;
    while (currentChar != '\n') {
        currentChar = fgetc(file_ptr);
        if (currentChar == 'S') {
            beams = Node_Construct(inpWidth, 1);
        }
        inpWidth++;
    }

    int row = 1;
    int col = 0;
    List* node = beams;
    List* lastNode = NULL;
    int splitCount = 0;
    unsigned long long int timelines = 0;

    while (currentChar != EOF) {
        node = beams;
        lastNode = NULL;
        for (col=0; col<inpWidth-1; col++) {
            currentChar = fgetc(file_ptr);
            if (node && col == node->col) {
                if (currentChar == '^') {
                    splitCount++;
                    if (node->next == NULL || node->next->col>col+1) {
                        List* newNode = Node_Construct(col+1, node->timelines);
                        newNode->next = node->next;
                        node->next = newNode;
                    } else if (node->next && node->next->col==col+1) {
                        node->next->timelines += node->timelines;
                    }
                    if (lastNode == NULL || lastNode->col<col-1) {
                        node->col = col-1;
                    } else if (lastNode && node->next) {
                        lastNode->next = node->next;
                        lastNode->timelines += node->timelines;
                        free(node);
                        node = lastNode->next;
                    }
                }
                lastNode = node;
                node = node->next;
            }
        }
        //Print_List(beams);
        fgetc(file_ptr);
        row++;
    }

    timelines = Print_List(beams);
    printf("There were %d splits and %llu timelines", splitCount, timelines);
    List_Destruct(beams);
    fclose(file_ptr);
    return 1;
}