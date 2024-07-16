#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include "linked_list.h"


list L;

int main(int argc, char *argv[]) {
    init_list(&L);
    //print_list(&L);
    delete_at_begin(&L);
    insert_at_begin(&L,3); 
    print_list(&L);
    delete_at_begin(&L);
    print_list(&L); 
    insert_at_begin(&L,3); 
    insert_at_begin(&L,2);
    insert_at_begin(&L,1);
    print_list(&L);
    delete_at_begin(&L);
    print_list(&L);
    //print_list(&L);
    insert_at_end(&L,4);
    insert_at_end(&L,5);
    insert_at_begin(&L,0);
    print_list(&L);
    delete_at_end(&L);
    delete_at_begin(&L);
    print_list(&L);
    delete_at_end(&L);
    print_list(&L);
    delete_at_end(&L);    
    delete_at_end(&L);
    printf("chao\n");    
    print_list(&L);
    delete_at_end(&L);
    // otra vez
    printf("------------------------------\n");
    insert_at_begin(&L,3); 
    insert_at_begin(&L,2);
    insert_at_begin(&L,1);
    insert_at_end(&L,4);
    insert_at_end(&L,5);
    print_list(&L);
    print_list2(&L);
    node *n = find_data(&L,1);
    printf("Valor: %d\n", n->data);
    n = find_data(&L,5);
    printf("Valor: %d\n", n->data);
    n = find_data(&L,2);
    printf("Valor: %d\n", n->data);
    n = find_data(&L,-2);
    if(n == NULL) {
        printf("Valor: No encontrado\n");
    }
    delete_data(&L, 1);
    print_list(&L);
    delete_data(&L, 4);
    print_list(&L);
    delete_data(&L, 3);
    print_list(&L);
    delete_data(&L, 5);
    print_list(&L);
    delete_data(&L, 5);
    print_list(&L);
    delete_data(&L, 2);
    print_list(&L);
    return 0;
}


