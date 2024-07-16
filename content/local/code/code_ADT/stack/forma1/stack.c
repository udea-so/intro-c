#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

void init_stack(stack *s) {
    s->top = NULL;
}

int push(stack *s, int data) {
    node *new = malloc(sizeof(node));
    if (new == NULL) {
        perror("malloc");
        return -1;
    }
    else {
        new->data = data;
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

int pop(stack *s) {    
    node *popped;
    int data;
    if (s->top == NULL) {
        printf("Empty Stack\n");
        return;
    }
    else {        
        popped = s->top;
        data = popped->data;        
        s->top = s->top->next;
        free(popped);
        return data;
    }
}

int peek(stack *s) {
    if(s->top != NULL) {
        return s->top->data;     
    }
    else {
        printf("Empty Stack\n");
        return; 
    }
} 

void print_stack(stack *s) {
    node *current = s->top;
    if (current == NULL) {
        printf("Empty Stack.\n");
        return;
    } 
    else { 
        while (current) {
            printf("| %6d |\n", current->data);
            current = current->next;
        } 
        printf("----------\n");
    } 
}