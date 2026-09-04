public class DoublyLinkedList {

    class Node {
        int data;
        Node prev;
        Node next;

        Node(int data) {
            this.data = data;
            this.prev = null;
            this.next = null;
        }
    }

    Node head;
    Node tail;
    int size;

    DoublyLinkedList() {
        head = null;
        tail = null;
        size = 0;
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return head == null;
    }

    public int first() {
        if (isEmpty())
            return -1;
        return head.data;
    }

    public int last() {
        if (isEmpty())
            return -1;
        return tail.data;
    }

    public void addFirst(int data) {
        Node newNode = new Node(data);

        if (isEmpty()) {
            head = tail = newNode;
        } else {
            newNode.next = head;
            head.prev = newNode;
            head = newNode;
        }

        size++;
    }

    public void addLast(int data) {
        Node newNode = new Node(data);

        if (isEmpty()) {
            head = tail = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }

        size++;
    }

    public int removeFirst() {
        if (isEmpty())
            return -1;

        int value = head.data;

        if (head == tail) {
            head = tail = null;
        } else {
            head = head.next;
            head.prev = null;
        }

        size--;
        return value;
    }

    public int removeLast() {
        if (isEmpty())
            return -1;

        int value = tail.data;

        if (head == tail) {
            head = tail = null;
        } else {
            tail = tail.prev;
            tail.next = null;
        }

        size--;
        return value;
    }
    // Insert at Position
public void insertAtPosition(int data, int pos) {

    if (pos < 1 || pos > size + 1) {
        System.out.println("Invalid Position");
        return;
    }

    if (pos == 1) {
        addFirst(data);
        return;
    }

    if (pos == size + 1) {
        addLast(data);
        return;
    }

    Node newNode = new Node(data);
    Node temp = head;

    for (int i = 1; i < pos - 1; i++) {
        temp = temp.next;
    }

    newNode.next = temp.next;
    newNode.prev = temp;

    temp.next.prev = newNode;
    temp.next = newNode;

    size++;
}
   // Delete at Position
public int deleteAtPosition(int pos) {

    if (isEmpty() || pos < 1 || pos > size)
        return -1;

    if (pos == 1)
        return removeFirst();

    if (pos == size)
        return removeLast();

    Node temp = head;

    for (int i = 1; i < pos; i++) {
        temp = temp.next;
    }

    int value = temp.data;

    temp.prev.next = temp.next;
    temp.next.prev = temp.prev;

    size--;

    return value;
}
// Reverse Doubly Linked List
public void reverse() {

    Node temp = null;
    Node current = head;

    tail = head;

    while (current != null) {

        temp = current.prev;
        current.prev = current.next;
        current.next = temp;

        current = current.prev;
    }

    if (temp != null) {
        head = temp.prev;
    }
}

}
