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
void List_init(list *);
int List_empty(list *);
void List_insert_at_begin(list *, int);
void List_insert_at_end(list *, int);
void List_print(list *, int);
int List_length(list *);
int List_delete_at_begin(list *);
int List_delete_at_end(list *);
node* List_lookup(list *, int);
int List_delete_item(list *L, int item);
void List_clean(list *L);

int main() {
    list *L = (list *)malloc(sizeof(list)); 
    List_init(L);
    List_insert_at_end(L, 1);
    List_insert_at_end(L, 2);
    List_insert_at_end(L, 3);
    List_insert_at_end(L, 4);
    List_insert_at_end(L, 5);
    printf("Lista inicial: ");
    List_print(L,1);
    List_delete_at_begin(L);
    printf("Lista al borrar el primer elemento (1): ");
    List_print(L,1);
    List_delete_at_end(L);
    printf("Lista al borrar ultimo elemento elemento (5): ");
    List_print(L,1);
    printf("Lista al borrar el elemento de la mitad (3): ");
    List_delete_item(L, 3);
    List_print(L,1);
    List_clean(L);
    printf("Lista al ser limpiada: ");
    List_print(L,1);
    free(L);
    return 0;
}

void List_init(list *L) {
    L->head = NULL;
}

list* List_new(void) {
    list *L = malloc(sizeof(L));
    assert(L != NULL);
    L->head = NULL;
    return L;
}



int List_empty(list *L) {
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

int List_delete_item(list *L, int item) {
    assert(L != NULL);
    if (L->head == NULL) {
        printf("ERROR: Empty List\n");
        return -1;
    }
    node *current = L->head;
    node *prev;
    while(current->next != NULL) {
        if(current->item == item) {
            if(current == L->head) {
                // First node
                L->head = current->next;
                free(current);                
            }
            else {
                prev->next = current->next;
                free(current);
            }
            return 0;
        }            
        prev = current;
        current = current->next;
    }
    if(current->item == item) {
        // Last node
        prev->next = NULL;
        free(current);
        return 0;        
    }
    printf("ERROR: Value not found\n");
    return -1;
}

void List_clean(list *L) {
    int len = List_length(L);
    for(int i = 0; i < len; i++) {
        List_delete_at_begin(L);
    }
}