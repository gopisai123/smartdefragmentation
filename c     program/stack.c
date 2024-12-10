#include <stdio.h>
#include <stdlib.h>
#define MAX 5  // Define maximum size of stack

// Stack structure
int stack[MAX];
int top = -1;

// Function to push an element onto the stack
void push(int value) {
    if (top == MAX - 1) {
        printf("Stack Overflow\n");
    } else {
        stack[++top] = value;
        printf("%d pushed onto stack\n", value);
    }
}

// Function to pop an element from the stack
int pop() {
    if (top == -1) {
        printf("Stack Underflow\n");
        return -1;
    } else {
        int popped_value = stack[top--];
        return popped_value;
    }
}

// Function to display the stack elements
void display() {
    if (top == -1) {
        printf("Stack is empty\n");
    } else {
        printf("Stack elements are: ");
        for (int i = 0; i <= top; i++) {
            printf("%d ", stack[i]);
        }
        printf("\n");
    }
}

// Main function to test the stack
int main() {
    push(10);
    push(20);
    push(30);
    push(40);
    push(50);
    display();

    printf("%d popped from stack\n", pop());
    display();

    return 0;
}


//linked list 
