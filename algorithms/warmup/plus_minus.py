# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())
nums = raw_input().split()
nums = map(int, nums)

plus = 0
minus = 0
zero = 0
for num in nums:
    if num > 0:
        plus += 1
    elif num < 0:
        minus += 1
    else:
        zero += 1
print round(plus/float(N), 3)
print round(minus/float(N), 3)
print round(zero/float(N), 3)
