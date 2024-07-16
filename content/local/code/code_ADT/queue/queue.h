#ifndef QUEUE_H
#define QUEUE_H

#include "node.h"

typedef struct _queue {
    node *head;
    node *tail;
} queue;

void init_queue(queue *q);
void enqueue(queue *q,  int data);
int dequeue(queue *q, int data); 
void print_queue(queue *q);

/*
void init_list(list *L);
int get_length(list *L);
void print_list(list *L);
void print_list2(list *L);
int insert_at_begin(list *L, int data);
int insert_at_end(list *L, int data);
int delete_at_begin(list *L); 
int delete_at_end(list *L); 
node* find_data(list *L, int data);
int delete_data(list *L, int data);
int is_empty(list *L);
*/

#endif

