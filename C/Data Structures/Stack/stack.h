/**
 * Stack Implementation.
 * 
 * @author Ben Antonellis
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 5

int stack[MAX_SIZE];
int top = -1;

void StackPush() {
    int value;
    printf("Enter value: ");
    scanf("%d", &value);
    top++;
    stack[top] = value;
}

void StackPop() {
    top--;
}

void StackPrint() {
    for (int i = top; i >= 0; i--) {
        printf("%d ", stack[i]);
    }
    printf("\n");
}