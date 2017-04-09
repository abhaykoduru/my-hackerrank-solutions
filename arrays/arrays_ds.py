#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

for each in range(n):
    arr.insert(each, arr[n-1])
    arr.pop()
    
print ' '.join(map(str, arr))
