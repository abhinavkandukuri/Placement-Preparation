
public class Day2LL {

    Node head;
    Node tail;

    class Node {

        int data;
        Node prev = null;
        Node next = null;

        Node(int data) {
            this.data = data;
        }
    }

    public void append(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
            tail = newNode;
        }

        tail.next = newNode;
        newNode.prev = tail;
        tail = newNode;
    }

    public void prpend(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
            tail = newNode;
        }

        newNode.next = head;
        head.prev = newNode;
        head = newNode;
    }

    public void deletefirst() {
        if (head == null) {
            System.out.println("The list is Empty");
        }
        if (head == tail) {
            head = null;
            tail = null;
        }
        head = head.next;
        head.prev = null;
    }

    public void deleteend() {
        if (head == null) {
            System.err.println("List is Empty");
        }
        if (head == tail) {
            head = null;
            tail = null;
        }
        tail = tail.prev;
        tail.next = null;
    }

    public void printll() {
        Node temp = head;

        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
    }

    public static void main(String[] args) {

        Day2LL list = new Day2LL();

        list.append(10);
        list.append(20);
        list.append(30);
        list.append(40);

        list.printll();
    }
}
