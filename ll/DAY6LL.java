public class Day6LL {
    public static void main(String[] args) {
        String original = "racecar";
        int left = 0;
        int right = original.length() - 1;
        boolean res = true;
        while (left < right) {
            if (original.charAt(left) != original.charAt(right)) {
                res = false;
                break;
            }
            left++;
            right--;
        }
        System.out.println(res);
    }
}
