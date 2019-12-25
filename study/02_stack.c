#include <stdio.h>

#define MAX 100

int stack[MAX];
int top = -1;

void push (value) {
    if (top > MAX) {
        printf("\nSTACK OVERFLOW\n");
    } else {
        stack[++top] = value;
    }
}

int pop () {
    if (top < 0) {
        printf("\nSTACK OVERFLOW\n");
        return -1;
    } else {
        return stack[top--];
    }
}

void print_stack () {
    int i;

    printf("STACK : ");
    for (i = 0; i < top+1; i++) {
        printf("%d ", stack[i]);
    }
    printf("\n");
}

int main () {
    print_stack();

    push(1);
    push(2);
    push(3);
    print_stack();

    printf("POP : %d\n", pop());
    printf("POP : %d\n", pop());
    print_stack();

    return 0;
}
