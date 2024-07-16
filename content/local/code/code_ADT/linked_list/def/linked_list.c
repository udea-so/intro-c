
#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"

void init_list(list *L) {
    L->head = NULL;
    L->tail = NULL;
}

int insert_at_begin(list *L, int data) {
    node *new = malloc(sizeof(node));
    if (new == NULL) {
        perror("malloc");
        return -1;
    }
    else {
        new->data = data;
        if (L->head != NULL) {
            // El resto de los elementos
            new->next = L->head;
            L->head = new;
        }
        else {
            // Primer elemento
            new->next = NULL;
            L->tail = new;
            L->head = new;
            // L->tail = new->next;
        }
        return 0;
    }
}

int insert_at_end(list *L, int data) {
    node *new = malloc(sizeof(node));
    if (new == NULL) {
        perror("malloc");
        return -1;
    }
    else {
        new->data = data;
        if (L->head != NULL) {
            // El resto de los elementos
            new->next = NULL;
            L->tail->next = new;
            L->tail = new;
        }
        else {
            // Primer elemento
            new->next = NULL;
            L->tail->next = new;            
            L->tail = new;   
        }
        return 0;
    }    
}


/*
Obtener longitud
*/

int get_length(list *L) {
    node *current = L->head;
    int count = 0;
    while (current != NULL) {
        count++;
        current = current->next;
    }
    return count;
}


/*
Imprimir la lista
*/
void print_list(list *L) {
    node *current = L->head;
    if (current == NULL) {
        printf("Empty list.\n");
        return;
    } 
    else {
        for(; current->next != NULL; current = current->next) {
            printf("[%d|%p] -> ", current->data, current->next);
        }
        printf("[%d|%p]\n", current->data, current->next);
    } 
}

void print_list2(list *L) {
    node *current = L->head;
    if (current == NULL) {
        printf("Empty list.\n");
        return;
    } 
    else { 
        while (current) {
            printf("[%d] -> ", current->data);
            current = current->next;
        } 
        printf("[X]\n");
    } 
}


int delete_at_begin(list *L) {    
    if (L->head == NULL) {
        printf("ERROR: Empty List\n");
        return -1;
    }
    else {
        node *current = L->head;
        L->head = current->next;
        free(current);
    }
}

int delete_at_end(list *L) {
    if (L->head == NULL) {
        printf("ERROR: Empty List\n");
        return -1;
    }
    else {
        node *current = L->tail;
        node *prev = L->head;
        if(current == prev) {
            // Solo hay un elemento
            free(current);
            L->head = NULL;
            L->tail = NULL;
        }
        else {
            while(prev->next != L->tail) {
                prev = prev->next;
            }        
            prev->next = NULL;
            L->tail = prev;
            free(current);
        }        
        return 0;
    }
}

node* find_data(list *L, int data) {
    node *current = L->head;
    while (current) {
        if (current->data == data) {
            return current; // success
        }
        current = current->next;
    }
    return NULL; // failure
}

int delete_data(list *L, int data) {
    // Head
    if(L->head->data == data ) {
        node *tmp = L->head;
        L->head = L->head->next;
        free(tmp);
        return 0;
    }
    // Others
    node *prev, *current;
    for(current = L->head; current->next != NULL; current = current->next) {
        if(current->data == data) {
            prev->next = current->next;
            free(current);
            return 0;
        }
        prev = current;
    }
    // Tail
    if(current == L->tail && current->data == data) {
        L->tail = prev;
        L->tail->next = NULL;
        free(current);
        return 0;
    }
    return -1;
}

int is_empty(list *L) {
    if(L->head == NULL && L->tail == NULL) {
        return 1; // Lista vacia
    }
    else {
        return 0; // Lista no vacia
    }
};

/*
void Push(struct node **headRef, int data) {
    struct node *newNode = malloc(sizeof(struct node));
    newNode->data = data;
    newNode->next = *headRef; // The '*' to dereferences back to the real head
    *headRef = newNode;       // ditto
}
*/


/*

int delete_at_front(struct node **phead) {
    struct node * first = *phead;
    assert(first != NULL);
    *phead = first->next;
    int data = first->data;
    free(first);
    return data;
}

void delete_at_begin(struct node **phead) {
    struct node *first = *phead;
    *phead = (*phead)->next;
    free(first);
}

struct node *insert_at_end(struct node *head, int data) {
    // create a new node.
    struct node * new_node = malloc(sizeof(struct node));
    assert(new_node != NULL);
    new_node->data = data;
    new_node->next = NULL;

    // list is empty.
    if (head == NULL) {
        head = new_node;
        return head;    
    }

    // list has some elements already.
    struct node *current = head;
    while (current->next != NULL) {
        current = current->next;
    }

    current->next = new_node;
    return head;
}

void print_list(struct node *head) {
    struct node * current = head;
    if (current == NULL) {
        printf("Empty list.\n");
        return;
    } else {
        while (current) {
            printf("|%d|%p| -> ", current->data, current->next);
            current = current->next;
        } 
        printf("\n");
    } 
}


*/