//both int and pointer variable also takes 4 bytes 
//the first node in the linked list is the head node , not the head pointer 
// #include<stdio.h>
// #include<stdlib.h>
// struct Node {
//     int data;
//     struct Node* next; //in cpp just Node* link 
// };
// struct Node* head = NULL; // global value can be acessable to all those given functions 
// void insrt(int x);
// void pri();
// int main () {
//     int n,x;
//     scanf("%d",&n);
//     for(int i=0;i<n;i++) {
//         scanf("%d",&x);
//         insrt(x);
//         pri();
//     }
//     return 0;
// }
// void insrt(int x ) {
//     struct Node* temp =  (struct Node*)malloc (sizeof(struct Node));
//     temp -> data = x;
//     temp -> next = head;
//     head = temp ;
// }
// void pri() {
//     struct Node* val = head;
//     while(val!= NULL) {
//         printf("%d ",val-> data);
//         val = val->next;

//     }

// }// refrence freecodecamp

//insert node at nth position 
// #include<stdio.h>
// #include<stdlib.h>
// struct Node {
//     int data;
//     struct Node* next;
// };
// struct Node* head = NULL;
// void insrt(int n,int a) ;
// void pri();
// int main() {
//     insrt(2,1);
//     insrt(3,2);
//     insrt(4,1);
//     insrt(5,2);
//     pri();
//     return 0;
// }
// void insrt(int n, int a) {
//     struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
//     temp -> data = n;
//     if(a==1) {
//         temp -> next = head;
//         head = temp ;
//     }
//     else {
//         struct Node* temp1 = head;
//         for(int i=0;i<a-2;i++) {
//             temp1 = temp1 -> next; 
            
//         }
//         temp-> next = temp1-> next ;
//         temp1->next = temp;
//     }
// }
// void pri()  {
//     struct Node* temp3 = head ;
//     while(temp3!= NULL ) {
//         printf("%d ",temp3-> data);
//         temp3 = temp3-> next;

//     }
// }
//study the application memory for above one 


//delete node at nth position 
// #include<stdio.h>
// #include<stdlib.h>
// struct Node {
//     int data;
//     struct Node* next;
// };
// void insert(int n);
// void pri();
// void delete(int n);
// struct Node* head = NULL;
// int main() {
//     head = NULL;
//     insert(2);
//     insert(4);
//     insert(6);
//     insert(5);
//     pri();
//     struct Node* ct = head;
//     int x =0;
//     while(ct!= NULL) {
//         x++;
//         ct = ct-> next;

//     }
//     int n;
//     scanf("%d",&n);
//     if(n>x || n<0) {
//         printf("invalid position");
//     }
//     else {
//         delete(n);
//         pri();

//     }
//     return 0;
// }
// void insert(int n) {
//     struct Node* temp = (struct Node*)malloc(sizeof(struct Node));


//     if(head == NULL ) {
//         temp -> data = n;
//         temp -> next = NULL;
//         head = temp;
//     }
//     else {
//         temp -> data = n;
//         temp -> next = NULL;

//         struct Node* temp1 = head;
//         while(temp1-> next != NULL ) {
//             temp1= temp1->next;
//         }
//         temp1 -> next = temp;
//     }

// }
// void pri() {
//     struct Node* t2 = head;
//     while (t2 != NULL) {
//         printf("%d ", t2->data);
//         t2 = t2-> next;
//     }
//     printf("\n");
    
// }
// void delete(int a) {
//     struct Node* t3= head;
//     if( a ==1) {
//         head = head -> next;
//         free(t3);
//     }
//     for(int i=0;i<(a-2);i++)  {
//         t3 = t3-> next;
//     }
//     struct Node* t4 = t3->next; //adress of node to get deleted 
//     t3 -> next = t4 -> next ;
//     free(t4);
// }


//reverse a link list
// #include<stdio.h>
// #include<stdlib.h>
// struct Node {
//     int data;
//     struct Node* next;
// };
// struct Node* head = NULL;
// void print() {
//     struct Node* temp2 =  head;
//     while (temp2!= NULL)  {
//         printf("%d ",temp2->data);
//         temp2 = temp2 -> next;
//     }
//     printf("\n");
// }
// void insert(int n)  {
//     struct Node* temp =  (struct Node*)malloc(sizeof(struct Node));
//     if( head == NULL) {
//         head = temp ;
//         temp -> data = n;
//         temp -> next = NULL;
//     }
//     else  {
//         temp -> data = n;
//         temp -> next = NULL;
//         struct Node* temp1 = head;
//         while (temp1-> next !=NULL) {
//             temp1 = temp1 -> next;
//         }
//         temp1 -> next = temp;

//     }
// }
// void reverse()  {
//     struct Node* curr  = head, *prev = NULL,*next;
//     while(curr != NULL) {
//         next = curr-> next;
//         curr -> next = prev;
        
//         prev = curr;
//         curr = next;
//     }
//     head = prev;
    
// }
// int main ()  {
//     insert(1);
//     insert(2);
//     insert(3);
//     insert(4);
//     insert(5);
//     print();
//     reverse();
//     print();
//     return 0;
// }


//double linked_list 
// each node contains 12 bytes 
#include<stdio.h>
#include<stdlib.h>
struct Node {
    int data;
    struct Node*next;
    struct Node*prev;
};
struct Node* head = NULL;
void insert(int x) {
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    temp-> data = x;
    temp -> prev = NULL;
    temp-> next = NULL;
    if(head == NULL)  {
        head = temp;
    }
    else {
        head -> prev = temp;
        temp->next = head;
        head = temp;
    }
}
void print()  {
    struct Node* temp = head;
    while (temp!= NULL) {
        printf("%d",temp->data);
        if(temp->next!=NULL)  {
            printf("->");
        }
        temp = temp->next;
       
    }
    printf("\n");

}
void reverse() {
    struct Node* temp = head;
    while(temp-> next!= NULL) {
        temp = temp-> next;

    }
    while (temp!=NULL)  {
        printf("%d",temp->data);
        if(temp->prev!=NULL) {
            printf("->");
        }
        temp = temp->prev;
    }
    printf("\n");
}
int main() {
    insert(8);
    insert(6);
    insert(7);
    print();
    print("\n");
    reverse();
    return 0;
}


