#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include "stack.h"

int main(int argc, char *argv[]) {
    stack S;
    init_stack(&S);
    peek(&S);
    push(&S,1);
    push(&S,2);
    push(&S,2);
    print_stack(&S);
    printf("\n**************\n\n");
    pop(&S);
    pop(&S);
    print_stack(&S);
    pop(&S);
    pop(&S);
    push(&S,10);
    push(&S,20);
    push(&S,30);
    print_stack(&S);
    printf("Top value = %d\n",peek(&S));
    return 0;
}