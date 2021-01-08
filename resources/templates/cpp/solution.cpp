#include <iostream>

int solve(int nums[], int n)
{
    int sum = 0;
    for (size_t i = 0; i < n; ++i)
        sum += nums[i];
    return sum;
}

int main()
{
    int n;
    std::cin >> n;
    int nums[n];
    for (size_t i = 0; i < n; ++i)
        std::cin >> nums[i];
    std::cout << solve(nums, n) << "\n";
    return 0;
}