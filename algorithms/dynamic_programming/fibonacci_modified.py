# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def call(a, b, n):
    if n==1:
        return a
    elif n==2:
        return b
    else:
        return int(pow(call(a, b, n-1),2)) + call(a, b, n-2)

def main():
	string=raw_input()
	a,b,n=map(int, string.strip().split())
	print call(a, b, n)
	
main()
