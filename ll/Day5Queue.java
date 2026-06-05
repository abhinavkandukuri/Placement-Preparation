import java.util.*;

public class Day4stack {

    public static int[] FINDGE(int[] arr) {
        int n = arr.length;
        int[] res = new int[n];
        Stack<Integer> stack = new Stack<>();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty()) {
                if (stack.peek() > arr[i]) {
                    res[i] = stack.peek();
                    break;
                } else {
                    stack.pop();
                }
            }
            if (stack.isEmpty()) {
                res[i] = -1;
            }
            stack.push(arr[i]);
        }
        return res;
    }
    public static void main(String[] args) {
        int[] arr = {4, 5, 2, 10};
        int[] ans = FINDGE(arr);
        for (int i = 0; i < ans.length; i++) {
            System.out.print(ans[i] + " ");
        }
    }
}
