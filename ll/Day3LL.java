
import java.util.*;

class Day3LL {

    public static void main(String[] args) {

        Stack<Integer> stack = new Stack<>();

        stack.push(10);
        stack.push(20);
        stack.push(30);

        System.out.println("Stack: " + stack + " -> LIFO Order");

        LinkedList<Integer> linkedList = new LinkedList<>();

        linkedList.add(10);
        linkedList.add(20);
        linkedList.add(30);

        System.out.println("LinkedList: " + linkedList + " -> Insertion Order");

        ArrayList<Integer> arrayList = new ArrayList<>();

        arrayList.add(10);
        arrayList.add(20);
        arrayList.add(30);

        System.out.println("ArrayList: " + arrayList + " -> Insertion Order");

        HashSet<Integer> hashSet = new HashSet<>();

        hashSet.add(30);
        hashSet.add(10);
        hashSet.add(20);

        System.out.println("HashSet: " + hashSet + " -> Unsorted");

        TreeSet<Integer> treeSet = new TreeSet<>();

        treeSet.add(30);
        treeSet.add(10);
        treeSet.add(20);

        System.out.println("TreeSet: " + treeSet + " -> Sorted");

        LinkedHashSet<Integer> linkedHashSet = new LinkedHashSet<>();

        linkedHashSet.add(30);
        linkedHashSet.add(10);
        linkedHashSet.add(20);

        System.out.println("LinkedHashSet: " + linkedHashSet + " -> Insertion Order");
    }
}
