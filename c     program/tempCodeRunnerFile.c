#include<stdio.h>
#include<stdlib.h>
struct Node {
    int data;
    struct Node* next; //in cpp just Node* link 
};
struct Node* head = NULL; // global value can be acessable to all those given functions 
void insrt(int x);
void pri();
int main () {
    int n,x;
    scanf("%d",&n);
    for(int i=0;i<n;i++) {
        scanf("%d",&x);
        insrt(x);
        pri();
    }
    return 0;
}
void insrt(int x ) {
    struct Node* temp =  (struct Node*)malloc (sizeof(struct Node));
    temp -> data = x;
    temp -> next = head;
    head = temp ;
}
void pri() {
    struct Node* val = head;
    while(val!= NULL) {
        printf("%d ",val-> data);
        val = val->next;

    }

}// refrence freecodecamp