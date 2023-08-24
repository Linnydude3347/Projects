#include <stdio.h>
#include "queue.h"

int main(int argc, char** argv) {

    int input;
    while (1) {
        printf("1. Insert\n");
        printf("2. Delete\n");
        printf("3. Print\n");
        printf("4. Exit\n");
        printf(">>> ");

        scanf("%d", &input);

        switch (input) {
            case 1: QueueInsert(); break;
            case 2: QueueDelete(); break;
            case 3: QueuePrint(); break;
            case 4: exit(1);
            default: printf("Invalid Option.\n");
        }
    }

    return 0;

}