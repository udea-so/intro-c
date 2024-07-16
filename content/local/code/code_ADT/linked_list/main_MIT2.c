#include <stdio.h>
#include <stdlib.h>

struct node { 
    int data; /* payload */ 
    struct node next ;
};

struct node head; /* beginning */


struct node *nalloc(int data);

int main(int argc, char * argv[]) {
    // |-> 2 -> 4 -> 6 -> 7 -> NULL
    return 0;
}

struct node *nalloc(int data) {
    struct node *p = (struct node *)malloc(sizeof(node));
    if (p != NULL)     {
        p->data = data;
        p->next = NULL;
    }
    return p;
}

struct node *addfront(struct node *head, int data) {
    struct node *p = nalloc(data);
    if (p == NULL)
        return head;
    p->next = head;
    return p;
}


/*

for ( p=head ; p!=NULL; p=p−>next ) 
   /∗ do something ∗/

for ( p=head ; p−>next != NULL; p=p−>next )
/∗ do something∗/

*/