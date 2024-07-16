#include <stdio.h>
#include "swap.h"

int main(int argc, char *argv[]) {
	int a = 6;
	int b = 1;
	printf("a: %d | b: %d\n", a, b);
	swap(&a, &b, sizeof a);
	printf("a: %d | b: %d\n", a, b);
}

