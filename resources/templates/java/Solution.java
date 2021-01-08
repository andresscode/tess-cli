import java.util.Scanner;

public class Solution {
    private static int solve(int[] nums) {
        int sum = 0;
        for (int num : nums)
            sum += num;
        return sum;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int nums[] = new int[n];
        for (int i = 0; i < n; ++i)
            nums[i] = scanner.nextInt();
        System.out.println(solve(nums));
    }
}