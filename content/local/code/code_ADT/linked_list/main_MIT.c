#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node* next;
};

typedef struct node node;

node* head = NULL; //Points to beginning of list. Set
                   // to null initially.

node* add_data(int data);
node * find_data(int data);
void rm_data(int data);

int main(int argc, char * argv[]) {
    // |-> 2 -> 4 -> 6 -> 7 -> NULL
    return 0;
}


// Adding new data to list
node* add_data(int data) {
    node* new_node = (node*) malloc(sizeof(node));
    new_node->data = data;
    new_node->next = head;
    head = new_node;
    return new_node;
}

// Searching through list
node * find_data(int data) {
    node* current;
    for( current = head; current->next!=NULL; current= current->next) {
        if(current->data == data) {
            return current;
        }
    }
    return NULL;
}

// Removing a certain data value
void rm_data(int data) {
    // Special case if the head has the data
    if (head->data == data) {
        node *tmp = head;
        head = head->next;
        free(tmp);
        return;
    }
    node *prev, *current;
    for (current = head; current->next != NULL; current = current->next) {
        if (current->data == data) {
                prev->next = current->next;
                free(current);
                return;
        }
        prev = current;
    }
}
