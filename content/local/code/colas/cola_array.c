#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define CAPACITY 4

typedef struct _queue {
    int count;
    int head;
    int tail;
    int list[CAPACITY];
} queue;

void Queue_init(queue *q);
int Queue_isEmpty(queue *q); 
int Queue_isFull(queue *q);
int Queue_size(queue *q);
int Queue_head(queue *q);
int Queue_back(queue *q);
void Queue_enqueue(queue *q,  int data);
int Queue_dequeue(queue *q, int *data);
void Queue_print(queue *q);
void Queue_clear(queue *q);


int main(int argc, char *argv[]) {
    queue Q;
    Queue_init(&Q);                      // La cola creada tiene 4 elementos --> [] -->
    if(Queue_isEmpty(&Q)) {
        printf("La cola esta vacia\n");
    }
    else if(Queue_isFull(&Q)) {
        printf("La cola esta llena\n");
    }
    printf("Tamaño de la cola Q: %d\n",Queue_size(&Q));
    // Agregando elementos a la cola
    Queue_enqueue(&Q, 19);               // --> [19] -->
    Queue_enqueue(&Q, 45);               // --> [45, 19] -->
    Queue_enqueue(&Q, 13);               // --> [13, 45, 19] -->
    Queue_enqueue(&Q, 7);                // --> [7, 13, 45, 19] -->
    // Despliegue de la cola
    Queue_print(&Q);
    // Mostrando el primer y ultimo elemento de la cola
    printf("Primer elemento de la cola: %d\n",Queue_head(&Q));
    printf("Ultimo elemento de la cola: %d\n",Queue_back(&Q));
    // Verificando si la cola esta llena
    if(Queue_isFull(&Q)) {
        printf("La cola esta llena\n");
    }
    // Encolando un dato cuando la cola esta llena
    Queue_enqueue(&Q, 21);
    // Sacando un dato de la cola (desencolar)
    int data;  // Valor en el que se llevara el dato sacado.
    Queue_dequeue(&Q, &data);            // --> [7, 13, 45] -->
    printf("Dato sacado de la cola: %d\n",data);
    // Despliegue de la cola
    Queue_print(&Q);
    // Encolando un nuevo dato
    data = 21;
    printf("Metiendo el %d a la cola \n", data);
    Queue_enqueue(&Q, data);              // --> [21, 7, 13, 45] -->
    Queue_print(&Q);
    // Vaciando la cola
    Queue_clear(&Q);
    if(Queue_isEmpty(&Q)) {
        printf("La cola esta vacia\n");
    }
    return 0;
}

void Queue_init(queue *q) {
    q->head = 0;
    q->tail = CAPACITY - 1;
    q->count = 0;
}

int Queue_isEmpty(queue *q) {
    return (q->count == 0);
} 

int Queue_isFull(queue *q) {
    return (q->count == CAPACITY);
} 

int Queue_size(queue *q) {
    return CAPACITY;
}

int Queue_head(queue *q) {
    assert(!Queue_isEmpty(q));
    return q->list[q->head];
}

int Queue_back(queue *q) {
    assert(!Queue_isEmpty(q));
    return q->list[q->tail];
}

void Queue_enqueue(queue *q,  int data) {  
  if(!Queue_isFull(q)) {
    q->tail = (q->tail + 1) % CAPACITY; 
    q->count++;
    q->list[q->tail] = data;   
  }
  else {
    printf("ERROR: Full queue\n");
  }
}


int Queue_dequeue(queue *q, int *data) {
    if (!Queue_isEmpty(q)) {
        q->count--;
        *data = q->list[q->head];
        q->head = (q->head + 1) % CAPACITY;
        return 0;
    }
    else {
        printf("ERROR: Empty queue\n");
        return -1;
    }
}


void Queue_print(queue *q) {
    if(Queue_isEmpty(q)) {
        printf("Empty queue.\n");
    }
    else {
        // head - tail
        if(q->head < q->tail) {
            printf("<-- ");
            for(int i = q->head; i <= q->tail; i++){
                printf("%4d    ", q->list[i]);
            }
            printf("<-- \n");            
        }
        else {
            int i;
            printf("<-- ");
            for(i = q->head; i < CAPACITY; i++){
                printf("%4d    ", q->list[i]);
            }
            for(i = 0; i <= q->tail; i++) {
                printf("%4d    ", q->list[i]);
            }
            printf("<-- \n");    
        }
    }
}

void Queue_clear(queue *q) {
  q->head = 0;
  q->tail = CAPACITY - 1;
  q->count = 0;
} 