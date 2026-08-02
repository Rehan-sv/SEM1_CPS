public class SinglyLinkedList {

    class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    Node head;
    Node tail;
    int size;

    SinglyLinkedList() {
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
            Node temp = head;

            while (temp.next != tail) {
                temp = temp.next;
            }

            temp.next = null;
            tail = temp;
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

        for (int i = 1; i < pos - 1; i++) {
            temp = temp.next;
        }

        int value = temp.next.data;
        temp.next = temp.next.next;

        size--;

        return value;
    }

    // Reverse List
    public void reverse() {

        Node prev = null;
        Node current = head;
        Node next;

        tail = head;

        while (current != null) {

            next = current.next;
            current.next = prev;

            prev = current;
            current = next;
        }

        head = prev;
    }
}