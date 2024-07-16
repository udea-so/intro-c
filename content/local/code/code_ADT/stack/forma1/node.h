#ifndef NODE_H
#define NODE_H

struct _node {
    int data;
    struct _node* next;
};

typedef struct _node node;


#endif