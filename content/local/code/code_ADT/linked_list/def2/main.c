#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef struct _node {
    int item;
    struct _node* next;
}node;

typedef struct _list {
    node *head;
} list;

list* List_new(void);
int List_init(list *);
void List_insert_at_begin(list *, int);
void List_insert_at_end(list *, int);
void List_print(list *, int);
int List_length(list *);
int List_delete_at_begin(list *);
int List_delete_at_end(list *);
node* List_lookup(list *, int);
void List_clean(list *L);

int main() {
    list *L = List_new();
    List_insert_at_begin(L, 1);
    List_print(L,1);
    List_insert_at_begin(L, 2);
    List_insert_at_begin(L, 3);
    List_print(L,2);
    List_insert_at_end(L, 0);
    List_print(L,1);
    List_print(L,2);
    List_delete_at_begin(L);
    List_print(L,1);
    List_delete_at_end(L);
    List_print(L,2);
    List_delete_at_end(L);
    List_print(L,1);
    List_delete_at_end(L);
    List_print(L,1);
    List_insert_at_end(L, 1);
    List_insert_at_end(L, 2);
    List_insert_at_end(L, 3);
    List_print(L,1);
    List_print(L,2);
    List_clean(L);
    List_print(L,1);
    return 0;
}


list* List_new(void) {
    list *L = malloc(sizeof(L));
    assert(L != NULL);
    L->head = NULL;
    return L;
}

int List_init(list *L) {
    assert(L != NULL);
    return (L->head == NULL);
}

void List_insert_at_begin(list *L, int item) {
    node *new = malloc(sizeof(node));
    assert(new != NULL);
    assert(L != NULL);
    new->item = item;
    if (L->head != NULL) {
        // El resto de los elementos
        new->next = L->head;
        L->head = new;
    }
    else {
        // Primer elemento
        new->next = NULL;
        L->head = new;
    }
}

void List_insert_at_end(list *L, int item) {
    node *new = malloc(sizeof(node));
    assert(new != NULL);
    assert(L != NULL);
    new->item = item;
    if (L->head == NULL) {
        new->next = L->head;
        L->head = new;
    }
    else {
        node *current = L->head;
        while (current->next != NULL) {
            current = current->next;
        }
        new->next = NULL;
        current->next = new;
    }    
}

int List_length(list *L) {
    node *current = L->head;
    int count = 0;
    while (current != NULL) {
        count++;
        current = current->next;
    }
    return count;
}


void List_print(list *L, int opt) {
    node *current = L->head;
    if (current == NULL) {
        printf("Empty list.\n");
    } 
    else {
        switch (opt)
        {
        case 1:
            while (current) {
                printf("[%d] -> ", current->item);
                current = current->next;
            } 
            printf("[X]\n");
            break;
        case 2:
            for(; current->next != NULL; current = current->next) {
                printf("[%d|%p] -> ", current->item, current->next);
            }
            printf("[%d|%p]\n", current->item, current->next);
            break;
        default:
            printf("Invalid option.\n");            
        }
    } 
}

int List_delete_at_begin(list *L) {    
    if (L->head == NULL) {
        printf("ERROR: Empty List\n");
        return -1;
    }
    else {
        node *current = L->head;
        L->head = current->next;
        free(current);
        return 0;
    }
}

int List_delete_at_end(list *L) {
    if (L->head == NULL) {
        printf("ERROR: Empty List\n");
        return -1;
    }
    else if(L->head->next == NULL) {
        free(L->head);
        L->head = NULL;
    }
    else {
        node *current = L->head;
        node *prev;
        while(current->next != NULL) {            
            prev = current;
            current = current->next;
        } 
        prev->next = NULL;
        free(current);       
        return 0;
    }
}

node* List_lookup(list *L, int item) {
    assert(L != NULL);
    node *current = L->head;
    while (current) {
        if (current->item == item) {
            return current; // success
        }
        current = current->next;
    }
    return NULL; // failure
}

void List_clean(list *L) {
    int len = List_length(L);
    for(int i = 0; i < len; i++) {
        List_delete_at_begin(L);
    }
}