/**
 * Queue Implementation.
 * 
 * @author Ben Antonellis
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 20
int queue[MAX_SIZE];
int front = -1;
int back = -1;

void QueueInsert() {
    int value;
    if (front == -1) {
        front = 0;
        printf("Enter value: ");
        scanf("%d", &value);
        back++;
        queue[back] = value;
    }
}

void QueueDelete() {
    front++;
}

void QueuePrint() {
    for (int i = 0; i <= back; i++) {
        printf("%d ", queue[i]);
    }
    printf("\n");
}
