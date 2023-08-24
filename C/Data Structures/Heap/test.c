#include <stdio.h>
#include "heap.h"

int main(int argc, char** argv) {

    int array[9] = {9, 8, 7, 6, 5, 4, 3, 2, 1};
    Heap* h = HeapCreate(9, array);
    HeapPrint(h);
    HeapExtractMin(h);
    HeapPrint(h);

    return 0;

}