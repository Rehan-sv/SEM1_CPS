package _Java.DSA;
import java.util.Scanner;

class Node {
    int pageId;
    String URL;
    String pageTitle;
    int timeStamp;
    Node prev;
    Node next;

    Node(int pageId, int timeStamp, String URL, String pageTitle) {
        this.pageId = pageId;
        this.timeStamp = timeStamp;
        this.URL = URL;
        this.pageTitle = pageTitle;
        this.prev = null;
        this.next = null;
    }
    // public Node getPrev() { return prev; }
    // public Node getNext() { return next; }
}

class Browser {
    int pageId;
    String URL;
    String pageTitle;
    int timeStamp;
    Browser(int pageId, int timeStamp, String URL, String pageTitle) {
        this.pageId = pageId;
        this.timeStamp = timeStamp;
        this.URL = URL;
        this.pageTitle = pageTitle;
    } 
}

class Traversal {
    Node current;
    Traversal(Node startNode) {
        this.current = startNode;
    }
    // public void forward() {
    //     if (current == null) {
    //         System.out.println("No history to move forward.");
    //         return;
    //     }
    //     if (current.prev == null) {
    //         System.out.println("Already at the most recent page: " + current.pageTitle);
    //     } else {
    //         current = current.prev;
    //         System.out.println("Forward -> " + current.pageId + " " + current.pageTitle);
    //     }
    // }
    // public void backward() {
    //     if (current == null) {
    //         System.out.println("No history to move backward.");
    //         return;
    //     }
    //     if (current.next == null) {
    //         System.out.println("Already at the oldest page: " + current.pageTitle);
    //     } else {
    //         current = current.next;
    //         System.out.println("Backward -> " + current.pageId + " " + current.pageTitle);
    //     }
    // }
}

class WebManagement {
    Node head;
    Node tail;
    int size;
    WebManagement() {
        head = null;
        tail = null;
        size = 0;
    }
    public Node getHead() {
        return head;
    }
    public void insert_f(int pageId, int timeStamp, String URL, String pageTitle) {
        Node newNode = new Node(pageId, timeStamp, URL, pageTitle);
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            newNode.next = head;
            head.prev = newNode;
            head = newNode;
        }
        size++;
        System.out.println("New Node has been added: " + pageTitle);
    }
    private void insert_end(int pageId, int timeStamp, String URL, String pageTitle) {
        Node newNode = new Node(pageId, timeStamp, URL, pageTitle);
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
        size++;
    }
    public void remove_by_Id(int Id) {
        Node temp = head;
        while (temp != null && temp.pageId != Id) {
            temp = temp.next;
        }
        if (temp == null) {
            System.out.println("Not found");
            return;
        }
        if (temp.prev != null) {
            temp.prev.next = temp.next;
        } else {
            head = temp.next;
        }
        if (temp.next != null) {
            temp.next.prev = temp.prev;
        } else {
            tail = temp.prev;
        }
        size--;
        System.out.println(Id + " has been removed");
    }
    public void del(int k) {
        if (k < 1 || k > size) {
            System.out.println("Invalid position");
            return;
        }
        Node curr = head;
        for (int i = 1; i < k; i++) {
            curr = curr.next;
        }
        if (curr.prev != null) {
            curr.prev.next = curr.next;
        } else {
            head = curr.next;
        }
        if (curr.next != null) {
            curr.next.prev = curr.prev;
        } else {
            tail = curr.prev;
        }
        size--;
        System.out.println("Deleted node at position " + k);
    }
    public void search(String URL) {
        Node temp = head;
        int k = 0;
        boolean found = false;
        while (temp != null) {
            if (temp.URL.equals(URL)) {
                System.out.println(URL + " found at position " + k);
                found = true;
                break;
            }
            temp = temp.next;
            k++;
        }
        if (!found) {
            System.out.println("Not found");
        }
    }
    public void display() {
        Node temp = head;
        while (temp != null) {
         System.out.println(temp.pageId + "    " + temp.pageTitle + "    " + temp.URL + "    " + temp.timeStamp);
            temp = temp.next;
        }
    }
    public void rev() {
        Node curr = head;
        Node temp = null;
        while (curr != null) {
            temp = curr.prev;
            curr.prev = curr.next;
            curr.next = temp;
            curr = curr.prev;
        }
        temp = head;
        head = tail;
        tail = temp;
        System.out.println("List reversed");
    }
    public WebManagement duplicate() {
        WebManagement newList = new WebManagement();
        Node temp = head;
        while (temp != null) {
            newList.insert_end(temp.pageId, temp.timeStamp, temp.URL, temp.pageTitle);
            temp = temp.next;
        }
        return newList;
    }
    public void del_from_k(int pos) {
        if (pos < 1 || pos > size) {
            System.out.println("Invalid position");
            return;
        }
        Node curr = head;
        for (int i = 1; i < pos; i++) {
            curr = curr.next;
        }
        if (curr.prev != null) {
            curr.prev.next = null;
            tail = curr.prev;
        } else {
            head = null;
            tail = null;
        }
        curr.prev = null;
        size = pos - 1;
        System.out.println("Deleted all nodes from position" + pos + "onward");
    }
}

public class BrowserHistory {
    public static void register(WebManagement wm, int pageId, int timeStamp, String URL, String pageTitle) {
        wm.insert_f(pageId, timeStamp, URL, pageTitle);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        WebManagement history = new WebManagement();
        Traversal nav = new Traversal(history.getHead());
        int choice = -1;
        while (choice != 0) {
            System.out.println("1. Insert new page ");
            System.out.println("2. Remove page by ID");
            System.out.println("3. Delete page at position");
            System.out.println("4. Search page by URL");
            System.out.println("5. Display history");
            System.out.println("6. Reverse history");
            System.out.println("7. Duplicate history");
            System.out.println("8. Delete from position to end");
            // System.out.println(" Move forward ");
            // System.out.println(" Move backward");
            System.out.println("0. Exit");
            System.out.print("Enter choice: ");
            choice = sc.nextInt();
            switch (choice) {
                case 1: {
                    System.out.print("Enter Page ID: ");
                    int pageId = sc.nextInt();
                    System.out.print("Enter Timestamp: ");
                    int timeStamp = sc.nextInt();
                    System.out.print("Enter URL: ");
                    String url = sc.next();
                    System.out.print("Enter Page Title: ");
                    String title = sc.next();
                    register(history, pageId, timeStamp, url, title);
                    nav.current = history.getHead();
                    break;
                }
                case 2: {
                    System.out.print("Enter Page ID to remove: ");
                    int id = sc.nextInt();
                    history.remove_by_Id(id);
                    break;
                }
                case 3: {
                    System.out.print("Enter position to delete: ");
                    int pos = sc.nextInt();
                    history.del(pos);
                    break;
                }
                case 4: {
                    System.out.print("Enter URL to search: ");
                    String url = sc.next();
                    history.search(url);
                    break;
                }
                case 5: {
                    history.display();
                    break;
                }
                case 6: {
                    history.rev();
                    break;
                }
                case 7: {
                    WebManagement copy = history.duplicate();
                    System.out.println("Duplicated history:");
                    copy.display();
                    break;
                }
                case 8: {
                    System.out.print("Enter position to delete from: ");
                    int pos = sc.nextInt();
                    history.del_from_k(pos);
                    break;
                }
                // case 9: {
                //     nav.forward();
                //     break;
                // }
                // case 10: {
                //     nav.backward();
                //     break;
                // }
                case 0: {
                    System.out.println("Exiting Browser History Manager.");
                    break;
                }
                default: {
                    System.out.println("Invalid choice, try again.");
                    break;
                }
            }
        }
        sc.close();
    }
}