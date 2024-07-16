#include <stdio.h>
#include "swap.h"

#define ARR_LEN 4
int main(int argc, char *argv[]) {
	int arr[ARR_LEN] = {1, 4, 3, 4};
	printf("arr: [%d, %d, %d, %d]\n", arr[0], arr[1], arr[2], arr[3]);
	swap_ends(arr, ARR_LEN, sizeof arr[0]);
	printf("arr: [%d, %d, %d, %d]\n", arr[0], arr[1], arr[2], arr[3]);
}

