#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define CAPACITY 4

typedef struct _queue {
    int count;
    int front;
    int rear;
    int list[CAPACITY];
} queue;

void Queue_init(queue *q);
int Queue_isEmpty(queue *q); 
int Queue_isFull(queue *q);
int Queue_size(queue *q);
int Queue_front(queue *q);
int Queue_back(queue *q);
void Queue_enqueue(queue *q,  int data);
int Queue_dequeue(queue *q, int *data);
void Queue_print(queue *q);

int main(int argc, char *argv[]) {
    queue Q;
    Queue_init(&Q);
    if(Queue_isEmpty(&Q)) {
        printf("La cola esta vacia\n");
    }
    else {
        printf("La cola tiene elementos\n");
    }
    printf("Tamaño Q: %d\n",Queue_size(&Q));
    // Agregando elementos a la cola
    
    Queue_enqueue(&Q, 19);
    Queue_enqueue(&Q, 45);
    Queue_enqueue(&Q, 13);
    Queue_enqueue(&Q, 7);
    Queue_print(&Q);
    printf("Primero: %d\n",Queue_front(&Q));
    printf("Ultimo: %d\n",Queue_back(&Q));
    Queue_enqueue(&Q, 21);
    int data;
    Queue_dequeue(&Q, &data);
    printf("Dato sacado: %d\n",data);
    Queue_print(&Q);
    Queue_enqueue(&Q, 21);
    Queue_print(&Q);

    /*
    printf("Tamaño Q: %d\n",Queue_size(Q));
    // Agregando elementos a la cola
    Queue_enqueue(Q, 19);
    Queue_enqueue(Q, 45);
    Queue_enqueue(Q, 13);
    Queue_enqueue(Q, 7);
    printf("Tamaño Q: %d\n",Queue_size(Q));
    // Queue_print(Q);
    int data;
    Queue_dequeue(Q, &data);
    printf("Dato sacado: %d\n",data);
    //Queue_print(Q);    
    Queue_dequeue(Q, &data);
    printf("Dato sacado: %d\n",data);
    //Queue_print(Q);    
    Queue_dequeue(Q, &data);
    printf("Dato sacado: %d\n",data);
    //Queue_print(Q);    
    Queue_dequeue(Q, &data);
    printf("Dato sacado: %d\n",data);
    //Queue_print(Q);    
    Queue_dequeue(Q, &data);
    printf("Dato sacado: %d\n",data);
    //Queue_print(Q);
    */

    /*
    Queue_init(&Q);
    Queue_print(&Q);
    Queue_enqueue(&Q, 1);
    Queue_enqueue(&Q, 2);
    Queue_print(&Q);
    */
    return 0;
}


void Queue_init(queue *q) {
    q->front = 0;
    q->rear = CAPACITY - 1;
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

int Queue_front(queue *q) {
    assert(!Queue_isEmpty(q));
    return q->list[q->front];
}

int Queue_back(queue *q) {
    assert(!Queue_isEmpty(q));
    return q->list[q->rear];
}

void Queue_enqueue(queue *q,  int data) {  
  if(!Queue_isFull(q)) {
    q->rear = (q->rear + 1) % CAPACITY; 
    q->count++;
    q->list[q->rear] = data;   
  }
  else {
    printf("ERROR: Full queue\n");
  }
}


int Queue_dequeue(queue *q, int *data) {
    if (!Queue_isEmpty(q)) {
        q->count--;
        *data = q->list[q->front];
        q->front = (q->front + 1) % CAPACITY;
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
        // front - rear
        if(q->front < q->rear) {
            printf("<-- ");
            for(int i = q->front; i <= q->rear; i++){
                printf("%4d    ", q->list[i]);
            }
            printf("<-- \n");            
        }
        else {
            int i;
            printf("<-- ");
            for(i = q->front; i < CAPACITY; i++){
                printf("%4d    ", q->list[i]);
            }
            for(i = 0; i <= q->rear; i++) {
                printf("%4d    ", q->list[i]);
            }
            printf("<-- \n");    
        }
    }
    /*
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
    */
}
