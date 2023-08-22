/**
 * Circular Buffer Implementation.
 * 
 * @author Ben Antonellis
*/

#include <stdbool.h>

typedef struct {
    int* buffer;
    int head;
    int tail;
    bool full;
    int MAX_SIZE;
} CircularBuffer;

#define CreateBuffer(name, max_size) \
    int name##_space[max_size]; \
    CircularBuffer name = { \
        .buffer = name##_space, \
        .head = 0, \
        .tail = 0, \
        .full = false, \
        .MAX_SIZE = max_size \
    }


void BufferPut(CircularBuffer b, int value) {
    b.buffer[b.head] = value;
    if (b.full) {
        b.tail = (b.tail + 1) % b.MAX_SIZE;
    }
    b.head = (b.head + 1) % b.MAX_SIZE;
    b.full = b.head == b.tail;
}


int BufferGet(CircularBuffer b) {
    int value = b.buffer[b.tail];
    b.full = false;
    b.tail = (b.tail + 1) % b.MAX_SIZE;
    return value;
}

void BufferReset(CircularBuffer b) {
    b.head = 0;
    b.tail = 0;
    b.full = false;
}