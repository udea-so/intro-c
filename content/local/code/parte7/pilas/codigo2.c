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
  stack_init(&S);    // S = [ ] : Lista vacia
  stack_push(&S, 1); // S = [|top|-> 1]
  stack_push(&S, 2); // S = [|top|-> 2 , 1]
  stack_push(&S, 3); // S = [|top|-> 3, 2 , 1]
  int e = stack_pop(&S); // S = [|top|-> 2 , 1] ; e = 3
  printf("Elemento sacado de la pila: %d\n", e);
  printf("Elementos disponibles en la pila: %d \n",  S.count);
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