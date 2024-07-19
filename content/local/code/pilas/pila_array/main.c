#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define CAPACITY 10

typedef struct _stack {
  int count;
  int data[CAPACITY];
} stack;

stack *stack_init(void);
int stack_empty(stack *);
void stack_push(stack *, int);
int stack_pop(stack *);
void print_stack(stack *s);

int main() {
  printf("Enlace\n");
  stack *S = stack_init();
  stack_push(S, 1);
  stack_push(S, 2);
  stack_push(S, 3);
  stack_push(S, 4);
  printf("valor sacado = %d\n",stack_pop(S));
  printf("valor sacado = %d\n",stack_pop(S));
  printf("valor sacado = %d\n",stack_pop(S));
  printf("valor sacado = %d\n",stack_pop(S));
  printf("valor sacado = %d\n",stack_pop(S));
  return 0;
}

stack *stack_init(void) { 
  stack *s = malloc(sizeof(s));
  assert(s!= NULL);
  s->count = 0;
  return s;
}

int stack_empty(stack *s) {
  assert(s != NULL);
  return (s->count == 0);
}

void stack_push(stack *s, int item) {
  assert(s != NULL);
  assert(s->count < CAPACITY);
  s->data[s->count] = item;
  s->count++;
}

int stack_pop(stack *s) {
  assert(s != NULL);
  assert(s->count > 0);
  s->count--;
  return s->data[s->count];
}

void print_stack(stack *s) {
    assert(s != NULL);
    if (s->count == 0){
        printf("Stack empty\n");
    }
    else {
        for(int i = 0; i < s->count; i++) {
            printf("| %6d |\n", s->data[i]);
        }
        printf("----------\n");
    }
}