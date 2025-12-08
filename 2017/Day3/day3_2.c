#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#define NUM 347991

typedef struct listnode {
	struct listnode *next;
	int value;
} Node;

static Node * Node_construct(int val) {
	Node * nd = malloc(sizeof(Node));
	nd -> value = val;
	nd -> next = NULL;
    //printf("%d\n", val);
	return nd;
}

int main() {
    Node* node1;
    Node* node2;
    Node* node3;
    Node* node4;
    Node* node5;

    int initial_list[9] = {1,2,4,5,10,11,23,25,26};
    Node* sum_list = Node_construct(initial_list[0]);
    node1 = sum_list;
    for (int i=1; i<9; i++) {
        sum_list -> next = Node_construct(initial_list[i]);
        sum_list = sum_list -> next;

        if (i==1) {
            node2 = sum_list;
        } else if (i==2) {
            node3 = sum_list;
        } else if (i==7) {
            node4 = sum_list;
        } else if (i==8) {
            node5 = sum_list;
        }
    }

    int level = 4;
    int corners[4] = {3, 5, 7, 10};
    int corner_index = 3;
    int generating_index = 11; // SET HERE
    int generating_sum = 0;

    Node* new_node;
    Node* temp;

    while (node5 -> value < NUM) {     
        generating_sum = 0;  
        switch (corners[corner_index]-generating_index) {
            case 1:
                generating_sum += node1 -> value;
                generating_sum += node2 -> value;
                generating_sum += node5 -> value;
                printf("%d -- %d\n", generating_sum, corners[corner_index]-generating_index);

                new_node = Node_construct(generating_sum);
                node5 -> next = new_node;

                node5 = node5 -> next;
                node4 = node4 -> next;
                node3 = node3 -> next;
                node2 = node2 -> next;
                temp = node1 -> next;
                free(node1);
                node1 = temp;
                break;
            case 0:
                generating_sum += node1 -> value;
                generating_sum += node5 -> value;

                printf("%d -- %d\n", generating_sum, corners[corner_index]-generating_index);

                new_node = Node_construct(generating_sum);
                node5 -> next = new_node;

                node5 = node5 -> next;
                node4 = node4 -> next;
                break;
            case -1:
                generating_sum += node1 -> value;
                generating_sum += node2 -> value;
                generating_sum += node4 -> value;
                generating_sum += node5 -> value;

                printf("%d -- %d\n", generating_sum, corners[corner_index]-generating_index);

                new_node = Node_construct(generating_sum);
                node5 -> next = new_node;

                node5 = node5 -> next;
                node4 = node4 -> next;

                corner_index += 1;
                corner_index %= 4;

                if (corner_index == 0) {
                    level = ceil(sqrt(generating_index + 1));
                    level += 1-(level%2);
                    for (int i=3; i>=0; i--) {
                        corners[i] = level*level - (3-i)*(level-1);
                    }
                    corners[3] += 1;
                }
                break;
            default:
                generating_sum += node1 -> value;
                generating_sum += node2 -> value;
                generating_sum += node3 -> value;
                generating_sum += node5 -> value;

                printf("%d -- %d\n", generating_sum, corners[corner_index]-generating_index);

                new_node = Node_construct(generating_sum);
                node5 -> next = new_node;

                node5 = node5 -> next;
                node4 = node4 -> next;
                node3 = node3 -> next;
                node2 = node2 -> next;
                temp = node1 -> next;
                free(node1);
                node1 = temp;
        }
        generating_index++;
    }
    return 1;
}