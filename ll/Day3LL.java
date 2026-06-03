
import java.util.*;

class Main {

    public static void main(String[] args) {

        Stack<Integer> stack = new Stack<>();

        stack.push(10);
        stack.push(20);
        stack.push(30);

        System.out.println(stack);

        LinkedList<Integer> linkedList = new LinkedList<>();
  
        linkedList.add(10);
        linkedList.add(20);
        linkedList.add(30);

        System.out.println(linkedList);

        ArrayList<Integer> arrayList = new ArrayList<>();

        arrayList.add(10);
        arrayList.add(20);
        arrayList.add(30);

        System.out.println(arrayList);
    }
}
