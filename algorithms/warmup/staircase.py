# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())

for n in range(1, N+1):
    print ((N-n) * " ") + (n * "#")
