// http://cslibrary.stanford.edu/103/LinkedListBasics.pdf 

#include <stdio.h>
#include <stdlib.h>


struct node {
    int data;
    struct node* next;
};


struct node* BuildOneTwoThree(void);
struct node* BuildTwoThree(void);
int Length(struct node *head);
int LengthForLoop(struct node *head);
void printList(struct node *head);
void LengthTest(void);
void LinkTest(void);
void WrongPush(struct node *head, int data);
void WrongPushTest(void);
void Push(struct node **headRef, int data);
void PushTest(void); 
void PushTest2(void);
void ChangeToNull(struct node **headRef);
void ChangeCaller(void);
struct node *BuildWithSpecialCase(void);


int main(int argc, char **argv){
    // LengthTest();

    //struct node* myList = BuildOneTwoThree();
    //struct node* myList = BuildTwoThree();
    //printList(myList);

    // LinkTest();

    // WrongPushTest();

    // PushTest();

    PushTest2();

    return 0;
}


/*
 Build the list {1, 2, 3} in the heap and store
 its head pointer in a local stack variable.
 Returns the head pointer to the caller.
*/
struct node* BuildOneTwoThree(void) {
    struct node* head = NULL;
    struct node* second = NULL;
    struct node* third = NULL;
    head = malloc(sizeof(struct node)); // allocate 3 nodes in the heap
    second = malloc(sizeof(struct node));
    third = malloc(sizeof(struct node));
    head->data = 1; // setup first node
    head->next = second; // note: pointer assignment rule
    second->data = 2; // setup second node
    second->next = third;
    third->data = 3; // setup third link
    third->next = NULL;
    // At this point, the linked list referenced by "head"
    // matches the list in the drawing.
    return head;
}

struct node* BuildTwoThree(void) {
    struct node* head = NULL;
    struct node* second = NULL;
    head = malloc(sizeof(struct node)); // allocate 3 nodes in the heap
    second = malloc(sizeof(struct node));
    head->data = 2; // setup first node
    head->next = second; // note: pointer assignment rule
    second->data = 3; // setup second node
    second->next = NULL;
    // At this point, the linked list referenced by "head"
    // matches the list in the drawing.
    return head;
}

/*
 Given a linked list head pointer, compute
 and return the number of nodes in the list.
*/
int Length(struct node *head) {
    struct node *current = head;
    int count = 0;
    while (current != NULL) {
        count++;
        current = current->next;
    }
    return count;
}

void printList(struct node *head) {
    struct node *current = head;
    printf("|-> ");
    while (current != NULL) {
        printf("%d -> ",current->data);        
        current = current->next;
    }
    printf("NULL\n");
}

void LengthTest(void) {
    struct node* myList = BuildOneTwoThree();
    int len = Length(myList); // results in len == 3
}


void LinkTest(void) {
    /*
     3-Step Link In operation which adds a single node to the front of a linked list. The 3 steps
     1. Allocate:
        
        struct node* newNode;
        newNode = malloc(sizeof(struct node));
        newNode->data = data_client_wants_stored;

     2. Link Next

        newNode->next = head;

     3. Link Head

        head = newNode;

    */ 
    struct node* head = BuildTwoThree(); // suppose this builds the {2, 3} list
    struct node* newNode;
    newNode = malloc(sizeof(struct node)); // allocate
    newNode->data = 1;
    newNode->next = head; // link next
    head = newNode; // link head
    // now head points to the list {1, 2, 3}
}

void WrongPush(struct node *head, int data) {
    struct node *newNode = malloc(sizeof(struct node));
    newNode->data = data;
    newNode->next = head;
    head = newNode; // NO this line does not work!
}

void WrongPushTest(void) {
    struct node* head = BuildTwoThree();
    // printList(head);
    WrongPush(head, 1); // try to push a 1 on front -- doesn't work
    // printList(head);
}

/*
 Takes a list and a data value.
 Creates a new link with the given data and pushes
 it onto the front of the list.
 The list is not passed in by its head pointer.
 Instead the list is passed in as a "reference" pointer
 to the head pointer -- this allows us
 to modify the caller's memory.
*/
void Push(struct node **headRef, int data) {
    /*
    The traditional method to allow a function to change its caller's memory is to 
    pass a pointer to the caller's memory instead of a copy

    So in this case, the value we want to change is struct node*, so we pass a struct node** instead. 
    The two stars (**) are a little scary, but really it's just a straight application of the rule. 
    It just happens that the value we want to change already has one star (*), so the parameter 
    to change it has two (**).
    */

    /*
    Changing a Pointer With A Reference Pointer: 
    Many list functions need to change the caller's head pointer. To do this in the C language, pass 
    a pointer to the head pointer. Such a pointer to a pointer is sometimes called a "reference pointer". 
    The main steps for this technique are:
    - Design the function to take a pointer to the head pointer. This is the standard technique in C — pass 
      a pointer to the "value of interest" that needs to be changed. To change a struct node*, 
      pass a struct node**.
    - Use '&' in the caller to compute and pass a pointer to the value of interest.
    - Use '*' on the parameter in the callee function to access and change the value of interest.
    */
    struct node *newNode = malloc(sizeof(struct node));
    newNode->data = data;
    newNode->next = *headRef; // The '*' to dereferences back to the real head
    *headRef = newNode;       // ditto
}

void PushTest(void) {
    struct node *head = BuildTwoThree(); // suppose this returns the list {2, 3}
    // printList(head);
    Push(&head, 1);                      // note the &
    // printList(head);
    Push(&head, 13);
    // printList(head);
    // head is now the list {13, 1, 2, 3}

}

void PushTest2(void) {
    struct node *head = NULL; // make a list with no elements
    Push(&head, 1);
    Push(&head, 2);
    Push(&head, 3);
    printList(head);
    // head now points to the list {3, 2, 1}
}

// Return the number of nodes in a list (while-loop version)
int LengthForLoop(struct node *head) {
    int count = 0;
    struct node *current;
    for (current = head; current != NULL; current = current->next) {
        count++;
    }
    return (count);
}

// Change the passed in head pointer to be NULL
// Uses a reference pointer to access the caller's memory
void ChangeToNull(struct node **headRef) {   // Takes a pointer to
                                             // the value of interest
    *headRef = NULL;                         // use '*' to access the value of interest
}

void ChangeCaller(void) {
    struct node *head1;
    struct node *head2;
    ChangeToNull(&head1); // use '&' to compute and pass a pointer to
    ChangeToNull(&head2); // the value of interest
    // head1 and head2 are NULL at this point
}


// Build — At Head With Push()
struct node *AddAtHead() {
    struct node *head = NULL;
    int i;
    for (i = 1; i < 6; i++) {
        Push(&head, i);
    }
    // head == {5, 4, 3, 2, 1};
    return (head);
}

struct node *BuildWithSpecialCase(void) {
    struct node *head = NULL;
    struct node *tail;
    int i;
    // Deal with the head node here, and set the tail pointer
    Push(&head, 1);
    tail = head;
    // Do all the other nodes using 'tail'
    for (i = 2; i < 6; i++) {
        Push(&(tail->next), i); // add node at tail->next
        tail = tail->next;      // advance tail to point to last node
    }
    return (head); // head == {1, 2, 3, 4, 5};
}

struct node *BuildWithDummyNode() {
    struct node dummy;          // Dummy node is temporarily the first node
    struct node *tail = &dummy; // Start the tail at the dummy.
                                // Build the list on dummy.next (aka tail->next)
    int i;
    dummy.next = NULL;
    for (i = 1; i < 6; i++)
    {
        Push(&(tail->next), i);
        tail = tail->next;
    }
    // The real result list is now in dummy.next
    // dummy.next == {1, 2, 3, 4, 5};
    return (dummy.next);
}
