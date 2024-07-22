#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

struct _node {
    int data;
    struct _node* next;
};

typedef struct _node node;

typedef struct _queue {
    node *head;
    node *tail;
} queue;

void Queue_init(queue *q);
int Queue_isEmpty(queue *q); 
int Queue_size(queue *q);
int Queue_front(queue *q);
int Queue_back(queue *q);
void Queue_enqueue(queue *q,  int data);
int Queue_dequeue(queue *q, int *data);
void Queue_print(queue *q);

int main(int argc, char *argv[]) {
    queue* Q = (queue*)malloc(sizeof(queue));
    assert(Q != NULL);
    Queue_init(Q);
    if(Queue_isEmpty(Q)) {
        printf("La cola esta vacia\n");
    }
    else {
        printf("La cola tiene elementos\n");
    }
    printf("Tamaño Q: %d\n",Queue_size(Q));
    Queue_init(Q);
    printf("Tamaño Q: %d\n",Queue_size(Q));
    // Agregando elementos a la cola
    Queue_enqueue(Q, 19);
    Queue_enqueue(Q, 45);
    Queue_enqueue(Q, 13);
    Queue_enqueue(Q, 7);
    printf("Tamaño Q: %d\n",Queue_size(Q));
    printf("Primer elemento de Q: %d\n",Queue_front(Q));
    printf("Ultimo elemento de Q: %d\n",Queue_back(Q));
    Queue_print(Q);
    int data;
    Queue_dequeue(Q, &data);
    printf("Dato sacado: %d\n",data);
    Queue_print(Q);    
    Queue_dequeue(Q, &data);
    printf("Dato sacado: %d\n",data);
    Queue_print(Q);    
    Queue_dequeue(Q, &data);
    printf("Dato sacado: %d\n",data);
    Queue_print(Q);    
    Queue_dequeue(Q, &data);
    printf("Dato sacado: %d\n",data);
    Queue_print(Q);    
    Queue_dequeue(Q, &data);
    printf("Dato sacado: %d\n",data);
    Queue_print(Q);

    /*
    Queue_init(&Q);
    Queue_print(&Q);
    Queue_enqueue(&Q, 1);
    Queue_enqueue(&Q, 2);
    Queue_print(&Q);
    */
    free(Q);
    return 0;
}

void Queue_init(queue *q){
    q->head = NULL;
    q->tail = NULL;
}

int Queue_isEmpty(queue *q) {
    if ((q->head == q->tail) & (q->head == NULL)) {
        return 1;
    }
    else {
        return 0;
    }
} 

int Queue_size(queue *q) {
    int tam = 0;
    if (q->head == NULL) {        
        return 0;
    } 
    else {      
      node *current = q->head;
      while (current) {
        tam++;
        current = current->next;
      } 
      return tam;
    } 
}

int Queue_front(queue *q) {
    assert(q->head != NULL);
    return q->head->data;
}

int Queue_back(queue *q) {
    assert(q->head != NULL);
    return q->tail->data;
}

void Queue_enqueue(queue *q,  int data) {  
  node *new = malloc(sizeof(node));
  assert(new != NULL);
  new->data = data;
  if (q->head != NULL) {
    // El resto de los elementos
    new->next = NULL;
    q->tail->next = new;
    q->tail = new;
  }
  else {
    // Primer elemento    
    new->next = NULL;        
    q->head = q->tail = new;   
  }
}


int Queue_dequeue(queue *q, int *data) {
    if (q->head == NULL) {
        printf("ERROR: Empty Queue\n");
        return -1;
    }
    else {
        node *current = q->head;
        q->head = current->next;
        *data = current->data;
        free(current);
        return 0;
    }
}

void Queue_print(queue *q) {
    node *current = q->head;
    if (current == NULL) {
        printf("Empty queue.\n");
        return;
    } 
    else { 
        printf("<-- ");
        while (current) {
            if(current) { 
                printf("%4d    ", current->data);
            }
            current = current->next;
        } 
        printf("<-- \n");
    } 
}