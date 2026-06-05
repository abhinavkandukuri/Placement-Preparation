

public class example {


//     public static int[] FINDGE(int[] arr) {
//         int n = arr.length;
//         int[] res = new int[n];
//         Stack<Integer> stack = new Stack<>();
//         for (int i = n - 1; i >= 0; i--) {
//             while (!stack.isEmpty()) {
//                 if (stack.peek() > arr[i]) {
//                     res[i] = stack.peek();
//                     break;
//                 } else {
//                     stack.pop();
//                 }
//             }
//             if (stack.isEmpty()) {
//                 res[i] = -1;
//             }
//             stack.push(arr[i]);
//         }
//         return res;
//     }

//     public static void main(String[] args) {
//         int[] arr = {4, 5, 2, 10};
//         int[] ans = FINDGE(arr);
//         for (int i = 0; i < ans.length; i++) {
//             System.out.print(ans[i] + " ");
//         }
//     }

    int[] queue = new int[5];
    int front = -1;
    int rear = -1;

    void enqueue(int value) {
        if ((rear + 1) % queue.length == front) {
            System.out.println("Queue is full");
            return;
        }

        if (front == -1)
            front = 0;

        rear = (rear + 1) % queue.length;
        queue[rear] = value;
    }

    void dequeue() {
        if (front == -1) {
            System.out.println("Queue is empty");
            return;
        }

        System.out.println("Deleted: " + queue[front]);

        if (front == rear) {
            front = -1;
            rear = -1;
        } else {
            front = (front + 1) % queue.length;
        }
    }

    void display() {
        if (front == -1) {
            System.out.println("Queue is empty");
            return;
        }

        int i = front;
        while (true) {
            System.out.print(queue[i] + " ");
            if (i == rear)
                break;
            i = (i + 1) % queue.length;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        example q = new example();

        q.enqueue(10);
        q.enqueue(20);
        q.enqueue(30);
        q.display();

        q.dequeue();
        q.display();

        q.enqueue(40);
        q.enqueue(50);
        q.enqueue(60);
        q.display();
    }
}


