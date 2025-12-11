#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct List {
    unsigned long long int low;
    unsigned long long int high;
    struct List* next;
} List;

List* Node_Construct(unsigned long long int low, unsigned long long int high) {
    List* node = malloc(sizeof(List));
    if (node == NULL) {return NULL;}
    node -> low = low;
    node -> high = high;
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

void Print_List(List * head) {
    List * p = head;
    while (p) {
        printf("%llu-%llu->", p -> low, p -> high);
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

    unsigned long long int lowLim;
    unsigned long long int highLim;
    List* freshRanges = NULL;

    unsigned long long int fresh = 0;
    
    fscanf(file_ptr, "%llu-%llu\n", &lowLim, &highLim);
    freshRanges = Node_Construct(lowLim, highLim);

    // Parse through all ranges in input
    while (fscanf(file_ptr, "%llu-%llu\n", &lowLim, &highLim) > 1) {
        List* node = freshRanges;
        // Insert new node at beginning
        if (lowLim < node->low) {
            //printf("NEW START NODE\n");
            List* new = Node_Construct(lowLim, highLim);
            new->next = node;
            freshRanges = new;
            node = new;
        } else {
            while (node) {
                // If low limit falls inside of an existing range
                if (lowLim >= node->low && lowLim-1 <= node->high) {
                    // Avoid nested ranges
                    if (node->high < highLim) {
                        //printf("MERGE\n");
                        node->high = highLim;
                    }
                    break;
                } else if (node->next) {
                    // If low limit falls between existing ranges
                    if (lowLim > node->high && lowLim < node->next->low) {
                        //printf("INSERT BETWEEN\n");
                        List* new = Node_Construct(lowLim, highLim);
                        new->next = node->next;
                        node->next = new;
                        node = new;
                        break;
                    }
                // If low limit will require a new end node
                } else if (node->next == NULL) {
                    //printf("NEW END NODE\n");
                    List* new = Node_Construct(lowLim, highLim);
                    node->next = new;
                    node = new;
                    break;
                }
                node = node->next;
            }
        }
        // Check if any ranges need to be merged or removed
        while (node->next && node->high >= node->next->low-1) {
            // If an existing node is absorbed by new node
            if (node->high >= node->next->high) {
                //printf("DELETE\n");
                List* delNode = node->next;
                node->next = delNode->next;
                free(delNode);
            // If an existing node needs to merge with new node
            } else if (node->high < node->next->high) {
                //printf("MERGE\n");
                node->high = node->next->high;
                List* delNode = node->next;
                node->next = delNode->next;
                free(delNode);
            }
        }
    }

    List* node = freshRanges;
    while (node) {
        // Verify that list is valid
        if (node->low > node->high || (node->next && node->high+1 > node->next->low)) {printf("FAILFAILFAIL\n");}
        fresh += (node->high - node->low) + 1;
        node = node->next;
    }

    printf("There are %llu fresh ingredients\n", fresh);
    List_Destruct(freshRanges);
    fclose(file_ptr);
    return 1;
}