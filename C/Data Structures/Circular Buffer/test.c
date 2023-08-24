#include <stdio.h>
#include "buffer.h"

int main(int argc, char** argv) {

    CreateBuffer(buffer, 10);
    BufferPut(buffer, 5);
    BufferPut(buffer, 6);
    BufferPut(buffer, 7);
    BufferGet(buffer);
    BufferReset(buffer);

    return 0;

}