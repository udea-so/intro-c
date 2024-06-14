#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dannymrock/UdeA-SO-Lab/blob/master/lab0/lab0b/parte7/intro_estructuras_de_datos.ipynb)

# In[1]:


get_ipython().system('pip install tutormagic')
get_ipython().run_line_magic('load_ext', 'tutormagic')


# # Conceptos previos - Repaso #

# ## Apuntadores ##

# In[8]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\nint main() {\n    int a = 0;\n    int *aPtr;\n    aPtr = &a;\n    *aPtr = 3;\n    return 0;\n}')


# In[17]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n#define NULL 0\n\nint main() {\n    int a = 3, b = 4;\n    int *p = &a;\n    int **pp = &p;\n    int ***ppp = &pp;\n    ***ppp = 5;\n    **ppp = &b;\n    **pp = 6;\n    return 0;\n}')


# ## Reserva dinámica de memoria ##

# In[15]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n#define NULL 0\nint main() {\n    int *ptr1 = (int *)malloc(sizeof(int));\n    int *ptr2 = NULL;\n    ptr2 = (int *)malloc(3*sizeof(int));\n    *ptr1 = 3;\n    *ptr2 = *ptr1 + 1;\n    *(ptr2 + 1) = *ptr1 + 2;\n    *(ptr2 + 2) = *ptr1 + 3;\n    free(ptr1);\n    ptr1 = NULL;\n    free(ptr2); \n    ptr2 = NULL;\n    return 0;\n}')


# In[63]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n#define NULL 0\n\nint main() {\n    int *arr[2];\n    arr[0] = (int*)calloc(4,sizeof(int)); \n    arr[1] = (int*)calloc(5,sizeof(int)); \n    int **pp;\n    pp = &arr[0];\n    *(arr[0] + 3) = 2;  \n    arr[0][1] = 5;\n    *(*pp + 2) = -3;\n    pp = &arr[1];\n    *(*pp + 1) = 3;\n    *(*(arr + 1) + 4) = 10;\n    free(arr[0]);\n    free(arr[1]);\n    arr[0] = NULL;\n    arr[1] = NULL;\n    pp = NULL;\n    return 0; \n}')


# In[71]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n\n#define NULL 0\n\nint main() {\n    int **pp = (int **)malloc(2*sizeof(int**)); \n    *(pp + 1) = (int *)malloc(3*sizeof(int));\n    pp[0] = (int *)malloc(4*sizeof(int));\n    pp[0][3] = 3;\n    *(*pp + 2) = -2;\n    *(pp[1] + 1) = 10;\n    *(*(pp + 1) + 2) = 30;\n    *(*pp + 1) = -12;  \n    free(pp[0]);\n    pp[0] = NULL;\n    free(*(pp + 1));\n    pp[1] = NULL;\n    pp = NULL;\n    return 0;\n}')


# In[115]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n#define NULL 0\n\nstruct nodo{\n    char *cad;\n    struct nodo **next_nodo;    \n};\n\ntypedef struct nodo nodo;\n\nint main() {\n    nodo *nodo1 = (nodo *)malloc(sizeof(nodo));\n    nodo1->cad = (char*)malloc(20*sizeof(char));\n    strcpy(nodo1->cad, "Lenguaje C");\n    nodo1->next_nodo = NULL;\n    nodo *nodo2 = (nodo *)malloc(sizeof(nodo));\n    nodo2->next_nodo = NULL;\n    nodo1->next_nodo = &nodo2;\n    nodo2->cad = (char*)malloc(20*sizeof(char));\n    strcpy(nodo2->cad, "Lenguaje Java");\n    nodo *nodo3 = (nodo *)malloc(sizeof(nodo));\n    nodo3->cad = (char*)malloc(20*sizeof(char));\n    strcpy(nodo3->cad, "Lenguaje Python");\n    nodo3->next_nodo = &nodo2;\n    nodo1->next_nodo = &nodo3;\n    nodo *temp = nodo1;\n    while(temp->next_nodo != NULL) {\n        printf("%s ---> ",temp->cad);\n        temp = *temp->next_nodo;      \n    }\n    printf(" %s ---> NULL\\n",temp->cad);\n    // Eliminando el nodo 3 (Mitad)\n    nodo1->next_nodo = &nodo2;\n    nodo3->next_nodo = NULL;    \n    free(nodo3);\n    nodo3 = NULL;\n    // Volviendo a imprimir lo que quedo\n    temp = nodo1;\n    while(temp->next_nodo != NULL) {\n        printf("%s ---> ",temp->cad);\n        temp = *temp->next_nodo;      \n    }\n    printf(" %s ---> NULL\\n",temp->cad);\n    // Eliminando los elementos restantes\n    temp = nodo1;\n    while(*temp->next_nodo != NULL) {\n        free(*temp->next_nodo); \n        *temp->next_nodo = NULL;\n    }\n    temp = nodo1;    \n    free(temp);\n    nodo1 = NULL;\n    temp = NULL;\n    return 0;\n}')


# In[ ]:





# # Estructuras de datos dinamicas #

# ## Listas enladas ##

# * Código tomado del libro de deitel y deitel.
# * Colocar el enlace en la nube.

# In[7]:


get_ipython().run_cell_magic('tutor', '-l c -k', '#include <stdio.h>\n\n\n#define NULL 0\n\n// self-referential structure                       \nstruct listNode {                                      \n   char data; // each listNode contains a character \n   struct listNode *nextPtr; // pointer to next node\n}; \n\ntypedef struct listNode ListNode; // synonym for struct listNode\ntypedef ListNode *ListNodePtr; // synonym for ListNode*\n\n// prototypes\nvoid insert(ListNodePtr *sPtr, char value);\nchar delete(ListNodePtr *sPtr, char value);\nint isEmpty(ListNodePtr sPtr);\nvoid printList(ListNodePtr currentPtr);\nvoid instructions(void);\n\nint main(void)\n{ \n   ListNodePtr startPtr = NULL; // initially there are no nodes\n   int empty = isEmpty(startPtr);\n   if(empty == 1) {\n       puts("Empty List");\n   }\n   puts("Add elements to list");\n   insert(&startPtr, \'A\');  // Add A: A\n   insert(&startPtr, \'B\');  // Add B: A -- B \n   insert(&startPtr, \'X\');  // Add X: A -- B -- X\n   printList(startPtr);     // Print list\'s elements\n   insert(&startPtr, \'Z\');  // Add Z: A -- B -- X -- Z\n   printList(startPtr);     // Print list\'s elements\n   delete(&startPtr,\'B\');   // Delete B: A -- X -- Z \n   delete(&startPtr,\'Z\');   // Delete Z: A -- X  \n   printList(startPtr);     // Print list\'s elements\n   return 0;\n} \n\n\n\n// insert a new value into the list in sorted order\nvoid insert(ListNodePtr *sPtr, char value)\n{ \n   ListNodePtr newPtr = malloc(sizeof(ListNode)); // create node\n\n   if (newPtr != NULL) { // is space available\n      newPtr->data = value; // place value in node\n      newPtr->nextPtr = NULL; // node does not link to another node\n\n      ListNodePtr previousPtr = NULL;\n      ListNodePtr currentPtr = *sPtr;\n\n      // loop to find the correct location in the list       \n      while (currentPtr != NULL && value > currentPtr->data) {\n         previousPtr = currentPtr; // walk to ...               \n         currentPtr = currentPtr->nextPtr; // ... next node \n      }                                          \n\n      // insert new node at beginning of list\n      if (previousPtr == NULL) { \n         newPtr->nextPtr = *sPtr;\n         *sPtr = newPtr;\n      } \n      else { // insert new node between previousPtr and currentPtr\n         previousPtr->nextPtr = newPtr;\n         newPtr->nextPtr = currentPtr;\n      } \n   } \n   else {\n      printf("%c not inserted. No memory available.\\n", value);\n   } \n} \n\n// delete a list element\nchar delete(ListNodePtr *sPtr, char value)\n{ \n   // delete first node if a match is found\n   if (value == (*sPtr)->data) { \n      ListNodePtr tempPtr = *sPtr; // hold onto node being removed\n      *sPtr = (*sPtr)->nextPtr; // de-thread the node\n      free(tempPtr); // free the de-threaded node\n      return value;\n   } \n   else { \n      ListNodePtr previousPtr = *sPtr;\n      ListNodePtr currentPtr = (*sPtr)->nextPtr;\n\n      // loop to find the correct location in the list\n      while (currentPtr != NULL && currentPtr->data != value) { \n         previousPtr = currentPtr; // walk to ...  \n         currentPtr = currentPtr->nextPtr; // ... next node  \n      } \n\n      // delete node at currentPtr\n      if (currentPtr != NULL) { \n         ListNodePtr tempPtr = currentPtr;\n         previousPtr->nextPtr = currentPtr->nextPtr;\n         free(tempPtr);\n         return value;\n      } \n   } \n\n   return \'\\0\';\n} \n\n// return 1 if the list is empty, 0 otherwise\nint isEmpty(ListNodePtr sPtr)\n{ \n   return sPtr == NULL;\n} \n\n// print the list\nvoid printList(ListNodePtr currentPtr)\n{ \n   // if list is empty\n   if (isEmpty(currentPtr)) {\n      puts("List is empty.\\n");\n   } \n   else { \n      puts("The list is:");\n\n      // while not the end of the list\n      while (currentPtr != NULL) { \n         printf("%c --> ", currentPtr->data);\n         currentPtr = currentPtr->nextPtr;   \n      } \n\n      puts("NULL\\n");\n   } \n} \n')


# In[ ]:




