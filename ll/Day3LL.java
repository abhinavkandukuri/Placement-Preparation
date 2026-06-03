import java.util.*;

class Day3LL {

    public static boolean checkDuplicatesM1(int n, int[] arr) {

        for (int i = 0; i < arr.length; i++) {

            for (int j = i + 1; j < arr.length; j++) {

                if (arr[i] == arr[j]) {
                    return true;
                }
            }
        }

        return false;
    }

    public static boolean checkDuplicatesM2(int n, int[] arr) {

        Set<Integer> hashSet = new HashSet<>();

        for (int i = 0; i < arr.length; i++) {

            if (hashSet.contains(arr[i])) {
                return true;
            } 
            else {
                hashSet.add(arr[i]);
            }
        }

        return false;
    }

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


        // Return true if value appears twice else false

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the number of elements: ");

        int n = sc.nextInt();

        int[] arr = new int[n];

        System.out.println("Enter the elements");

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        boolean res = checkDuplicatesM1(n, arr);

        System.out.println("Method1: " + res);

        boolean rese = checkDuplicatesM2(n, arr);

        System.out.println("Method2: " + rese);
    }
}
