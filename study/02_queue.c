#include <stdio.h>

#define MAX 3

int queue[MAX];
int front = 0, rear = 0;

void enqueue (value) {
    if (front == (rear+1) % MAX) {
        printf("QUEUE OVERFLOW, value = %d, front = %d, rear = %d\n", value, front, rear);
    } else {
        queue[rear] = value;
        rear = (rear+1) % MAX;
        printf("ENQUEUE : value = %d, front = %d, rear = %d\n", value, front, rear);
    }
}

int dequeue () {
    int value;
    if (front == rear) {
        printf("QUEUE EMPTY, front = %d, rear = %d\n", front, rear);
        return -1;
    } else {
        value = queue[front];
        front = (front+1) % MAX;
        return value;
    }
}

void print_queue () {
    int i;

    printf("QUEUE : ");
    for (i = front; i != rear; i = (i+1) % MAX) {
        printf("%d ", queue[i]);
    }
    printf("\n");
}

int main() {
    int value;

    print_queue();
    printf("\n");

    enqueue(1);
    enqueue(2);
    enqueue(3);
    print_queue();
    printf("\n");

    value = dequeue();
    if (value != -1) {
        printf("DEQUEUE : value = %d, front = %d, rear = %d\n", value, front, rear);
    }
    value = dequeue();
    if (value != -1) {
        printf("DEQUEUE : value = %d, front = %d, rear = %d\n", value, front, rear);
    }
    value = dequeue();
    if (value != -1) {
        printf("DEQUEUE : value = %d, front = %d, rear = %d\n", value, front, rear);
    }
    printf("\n");

    enqueue(1);

    printf("\n");
    print_queue();

    return 0;
}
