#include <stdio.h>
#include <stdlib.h>

#define ARR_LEN 4

void swap_ints(int *x, int *y);
void swap_floats(float *x, float *y);
void swap_strings(char **x, char **y);
void swap_ends(void *arr, size_t nelems, size_t nbytes);

int main(int argc, char *argv[]) {
    int a = 6;
    int b = 1;
    printf("a : % d | b : % d\n", a, b);
    swap(&a, &b, sizeof a);
    printf("a : % d | b : % d\n", a, b);
    // 
    int arr[ARR_LEN] = {1, 4, 3, 4};
    printf("arr: [%d, %d, %d, %d]\n", arr[0], arr[1], arr[2], arr[3]);
    swap_ends(arr, ARR_LEN, sizeof arr[0]);
    printf("arr: [%d, %d, %d, %d]\n", arr[0], arr[1], arr[2], arr[3]);
    return 0;

}

void swap_ints(int *x, int *y)
{
    int tmp = *x;
    *x = *y;
    *y = tmp;
}

void swap_floats(float *x, float *y)
{
    float tmp = *x;
    *x = *y;
    *y = tmp;
}

void swap_strings(char **x, char **y)
{
    char *tmp = *x;
    *x = *y;
    *y = tmp;
}

void swap(void *x, void *y, size_t nbytes)
{
    /* Save x in tmp
     * Copy value in y to x
     * Copy value in tmp to x        */
    char tmp[nbytes];       // Create space to hold x;
    memcpy(tmp, x, nbytes); // Save value of x in tmp
    memcpy(x, y, nbytes);   // Copy value in y to x
    memcpy(y, tmp, nbytes); // Copy value in tmp to y
}

void swap_ends(void *arr, size_t nelems, size_t nbytes) {
    void *start = arr;
    void *end   = (char *) arr + (nelems - 1) * nbytes; // void *end   = (__a__) arr + __b__;
    swap(start, end, nbytes);
} 
