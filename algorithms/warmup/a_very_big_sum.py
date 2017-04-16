# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())
nums = raw_input().split()
nums = map(int, nums)

result = 0
for num in nums:
    result += num

print result
