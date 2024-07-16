#ifndef STACK_H
#define STACK_H

#include "node.h"

typedef struct _stack {
    node *top;
} stack;

void init_stack(stack *s);
int push(stack *s, int data);
int pop(stack *s);
int peek(stack *s);
void print_stack(stack *s);

#endif

