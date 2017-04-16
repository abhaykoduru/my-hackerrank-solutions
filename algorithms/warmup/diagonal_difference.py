# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())
matrix = []
for everytime in range(N):
    temp = raw_input().split()
    temp = map(int, temp)
    matrix.append(temp)
sum1 = 0
sum2 = 0
for each in range(N):
    sum1 += matrix[each][each]
    sum2 += matrix[each][N-1-each]
diff = sum1 - sum2
diff = abs(diff)
print diff
