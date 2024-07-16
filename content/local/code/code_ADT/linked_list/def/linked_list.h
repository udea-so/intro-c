
#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include "node.h"

typedef struct _list {
    node *head;
    node *tail;
} list;


//int get_length(node *head);
//void print_list(node *head);

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

/*
int insert_at_begin(node *L, int data); 
*/


/*
void print_list(struct node *head);
struct node *insert_at_end(struct node *head, int data);
int delete_at_front(struct node **phead); 
*/

#endif

