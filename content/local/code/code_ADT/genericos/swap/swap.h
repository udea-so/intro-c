#include <string.h>

#ifndef MY_SWAP
#define MY_SWAP
#endif

void swap(void* x, void* y, size_t nbytes);

void swap_ends(void* arr, size_t nelems, size_t nbytes);
