def solve(nums):
    sum = 0
    for num in nums:
        sum = sum + num
    return sum

n = int(input())
nums = [int(num) for num in input().split()]

print(solve(nums))
