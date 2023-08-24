#include <stdio.h>
#include "stack.h"

int main(int argc, char** argv) {

    int input;
    while (1) {
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Print\n");
        printf("4. Exit\n");
        printf(">>> ");

        scanf("%d", &input);

        switch (input) {
            case 1: StackPush(); break;
            case 2: StackPop(); break;
            case 3: StackPrint(); break;
            case 4: exit(1);
            default: printf("Invalid Option.\n");
        }
    }

    return 0;

}