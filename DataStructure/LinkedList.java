class Node {
    Node next;
    Object data;
}

class App {
    Node head;

    Node get(Object data) {
        Node current = this.head;
        while (current.next != null) {
            if (current.data.equals(data)) {
                break;
            }
            current = current.next;
        }
        return current;
    }

    void insert(Object data) {
        Node newNode = new Node();
        newNode.data = data;

        if (this.head == null) {
            this.head = newNode;

        } else {
            Node current = this.head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    void insert(Node preNode, Object data) {
        Node newNode = new Node();
        newNode.data = data;

        newNode.next = preNode.next;
        preNode.next = newNode;
    }

    void delete() {
        if (this.head == null) {
            return;
        }
        if (this.head.next == null) {
            this.head = null;
            return;
        }

        Node preNode = this.head;
        Node current = preNode.next;

        if (current.next != null) {
            preNode = current;
            current = current.next;
        }

        preNode.next = null;
    }

    void delete(Object data) {
        if (this.head.data == data) {
            this.head = this.head.next;
            this.head.next = null;
            return;
        }

        Node preNode = this.head;
        Node current = preNode.next;

        while (current != null) {
            if (current.data == data) {
                preNode.next = current.next;
                current.next = null;
                break;
            }
            preNode = current;
            current = current.next;
        }
    }

    void print() {
        Node current = this.head;

        while (current != null) {
            System.out.println(current.data);
            current = current.next;
        }
    }
}

public class LinkedList {
    public static void main(String[] args) {
        App app = new App();

        app.insert("A");
        Node nodeA = app.get("A");
        app.insert(nodeA, "C");
        app.insert(nodeA, "B");
        app.print();

        System.out.println("#####");
        app.delete();
        app.print();

        System.out.println("#####");
        app.delete("B");
        app.print();
    }
}
