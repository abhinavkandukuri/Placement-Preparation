
public class Day1LL {

    Node head = null;

    public static class Node {

        int data;
        Node next = null;

        Node(int data) {
            this.data = data;
        }
    }

    public void append(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node currentNode = head;
            while (currentNode.next != null) {
                currentNode = currentNode.next;
            }
            currentNode.next = newNode;
        }
    }

    public void prepend(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    public void pois(int pos, int data) {
        if (pos == 0) {
            prepend(data);
        }
        Node temp = head;
        for (int i = 0; i < pos - 1 && temp != null; i++) {
            temp = temp.next;
        }
        if (temp == null) {
            System.out.println("Invalid Position");
            return;
        }
        Node newNode = new Node(data);
        newNode.next = temp.next;
        temp.next = newNode;
    }

    public void deletefirst() {
        if (head == null) {
            System.out.println("List is empty");
            return;
        } else {
            head = head.next;
        }
    }

    public void deletelast() {
        if (head == null) {
            System.out.println("List is empty");
        } else if (head.next == null) {
            head = null;
        } else {
            Node temp = head;
            while (temp.next.next != null) {
                temp = temp.next;
            }
            temp.next = null;
        }
    }

    public void delpois(int pos) {
        if (pos == 0) {
            deletefirst();
        }
        Node temp = head;
        for (int i = 0; i < pos - 1 && temp != null; i++) {
            temp = temp.next;
        }
        Node temp1 = temp;
        if (temp == null) {
            System.out.println("Invalid Position");
        }
        temp.next = temp1.next.next;

    }

    public void printll() {
        Node currNode = head;
        while (currNode != null) {
            System.out.print(currNode.data + " -> ");
            currNode = currNode.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        Day1LL ll = new Day1LL();
        ll.append(10);
        ll.append(20);
        ll.append(40);
        ll.prepend(30);
        ll.pois(2, 25);
        ll.printll();
        ll.deletefirst();
        ll.printll();
        ll.deletelast();
        ll.printll();
    }
}
