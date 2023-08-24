/**
 * Min Heap Implementation.
 * 
 * @author Ben Antonellis
*/

#include <stdio.h> // printf
#include <stdlib.h> // malloc

typedef struct heap {
    int* array;
    int size;
    int capacity;
} Heap;

Heap* HeapCreate(int, int*);
void HeapInsertHelper(Heap*, int);
void Heapify(Heap*, int);
int HeapExtractMin(Heap*);
void HeapInsert(Heap*, int);
void HeapPrint(Heap*);

Heap* HeapCreate(int capacity, int* values) {
    Heap* h = (Heap*)malloc(sizeof(Heap));
    h->size = 0;
    h->capacity = capacity;
    h->array = (int*)malloc(capacity * sizeof(int));
    int i;
    for (i = 0; i < capacity; i++) {
        h->array[i] = values[i];
    }
    h->size = i;
    i = (h->size - 2) / 2;
    while (i >= 0) {
        Heapify(h, i);
        i--;
    }
    return h;
}

void HeapInsertHelper(Heap* h, int index) {
    int parent = (index - 1) / 2;
    if (h->array[parent] > h->array[index]) {
        int temp = h->array[parent];
        h->array[parent] = h->array[index];
        h->array[index] = temp;
        HeapInsertHelper(h, parent);
    }
}

void Heapify(Heap* h, int index) {
    int left = index * 2 + 1;
    int right = index * 2 + 2;
    int min = index;
    if (left >= h->size || left < 0) {
        left = -1;
    }
    if (right >= h->size || right < 0) {
        right = -1;
    }
    if (left != -1 && h->array[left] < h->array[index]) {
        min = left;
    }
    if (right != -1 && h->array[right] < h->array[min]) {
        min = right;
    }
    if (min != index) {
        int temp = h->array[min];
        h->array[min] = h->array[index];
        h->array[index] = temp;
        Heapify(h, min);
    }
}

int HeapExtractMin(Heap* h) {
    int value = h->array[0];
    h->array[0] = h->array[h->size - 1];
    h->size--;
    Heapify(h, 0);
    return value;
}

void HeapInsert(Heap* h, int value) {
    if (h->size < h->capacity) {
        h->array[h->size] = value;
        HeapInsertHelper(h, h->size);
        h->size++;
    }
}

void HeapPrint(Heap* h) {
    for (int i = 0; i < h->size; i++) {
        printf("%d ", h->array[i]);
    }
    printf("\n");
}