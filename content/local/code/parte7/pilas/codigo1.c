#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define CAPACITY 3

typedef struct _stack {
  int count;
  int data[CAPACITY];
} stack;

void stack_init(stack *s);
int stack_empty(stack *s);
void stack_push(stack *s, int item);
int stack_pop(stack *s);
int stack_full(stack *s);
int stack_peek(stack *s);

int main() {
  stack S;
  stack_init(&S);
  if(stack_empty(&S) == 1) {
    printf("La pila esta vacia\n");
  }
  else if (stack_full(&S) == 1) {
    printf("La pila esta llena\n");
  }
  else {
    printf("En la pila aun caben %d elementos\n",CAPACITY - S.count);
  }
  stack_push(&S, 1);
  printf("Elemento agregado: %d\n", stack_peek(&S));
  stack_push(&S, 2);
  printf("Elemento agregado: %d\n", stack_peek(&S));
  if(stack_empty(&S) == 1) {
    printf("La pila esta vacia\n");
  }
  else if (stack_full(&S) == 1) {
    printf("La pila esta llena\n");
  }
  else {
    printf("En la pila aun caben %d elementos\n",CAPACITY - S.count);
  }
  stack_push(&S, 3);
  printf("Elemento agregado: %d\n", stack_peek(&S));
  if(stack_empty(&S) == 1) {
    printf("La pila esta vacia\n");
  }
  else if (stack_full(&S) == 1) {
    printf("La pila esta llena\n");
  }
  else {
    printf("En la pila aun caben %d elementos\n",CAPACITY - S.count);
  }
  return 0;
}

void stack_init(stack *s) { 
  s->count = 0;
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

int stack_full(stack *s) {
  assert(s != NULL);
  return (s->count == CAPACITY);
}

int stack_peek(stack *s) {
  assert(s != NULL);
  int top = s->data[s->count - 1];
  return top;
}