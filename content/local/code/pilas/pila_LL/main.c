#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

struct _node {
    char *data;
    struct _node* next;
};

typedef struct _node node;

typedef struct _stack {
    node *top;
} stack;

void Stack_init(stack *s);
int Stack_push(stack *s, char *data);
char* Stack_pop(stack *s);
char* Stack_peek(stack *s);
void Stack_print(stack *s);


int main() {
  stack s;
  Stack_init(&s);
  char *the_simpson[] = {
    "Bart",
    "Lisa",
    "Maggie"
  }; 
  printf("Agregando elementos a la pila:\n");
  Stack_push(&s, the_simpson[0]);
  Stack_push(&s, the_simpson[1]);
  Stack_push(&s, the_simpson[2]);
  Stack_print(&s);
  char *child = NULL;
  
  printf("\nElemento Top: %s\n",Stack_peek(&s));
  printf("Vaciando la pila:\n");
  child = Stack_pop(&s);
  printf("Elemento sacado -> %s\n",child);
  child = Stack_pop(&s);
  printf("Elemento sacado -> %s\n",child);
  child = Stack_pop(&s);
  printf("Elemento sacado -> %s\n",child);
  
  if(child != NULL) {
    free(child);
    child = NULL;
  }
  return 0;
}

void Stack_init(stack *s) {
    s->top = NULL;
}

int Stack_push(stack *s, char *data) {
    node *new = malloc(sizeof(node));
    if (new == NULL) {
        perror("malloc");
        return -1;
    }
    else {
        new->data = (char *)malloc((strlen(data) + 1)*sizeof(char));
        strcpy(new->data, data);
        if (s->top != NULL) {
            new->next = s->top;
        }
        else {
            new->next = NULL;
        }
        s->top = new;
        return 0;
    }
}

char* Stack_pop(stack *s) {    
    node *popped;
    char *data;
    if (s->top == NULL) {
        printf("Empty Stack\n");
        return NULL;
    }
    else {        
        popped = s->top;        
        s->top = s->top->next;
        data = strdup(popped->data);
        free(popped->data);
        free(popped);
        return data;
    }
}

char* Stack_peek(stack *s) {
    if(s->top != NULL) {
        return s->top->data;     
    }
    else {
        printf("Empty Stack\n");
        return NULL; 
    }
} 

void Stack_print(stack *s) {
    node *current = s->top;
    if (current == NULL) {
        printf("Empty Stack.\n");
        return;
    } 
    else { 
        while (current) {
            printf("| %10s |\n", current->data);
            current = current->next;
        } 
        printf("--------------\n");
    } 
}