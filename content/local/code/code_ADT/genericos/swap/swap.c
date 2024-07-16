#include <string.h>

void swap(void *x, void *y, size_t nbytes) {
	char tmp[nbytes];
	memcpy(tmp, x,   nbytes);
	memcpy(y,   x,   nbytes);
	memcpy(x,   tmp, nbytes);
}

void swap_ends(void* arr, size_t nelems, size_t nbytes) {
	void* start = arr;
	void* end = (char*) arr + (nelems - 1) * nbytes;

	swap(start, end, nbytes);
}
