#include <stdlib.h>

int main(int argc, char *argv[]) {
	for (;;) {
		int* leak = malloc(500 * sizeof *leak);
	}
}
