#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
apples, oranges = 0, 0

for ap in apple:
    if ap >= (s - a) and ap <= (t - a):
        apples += 1
        
for o in orange:
    if o <= (t - b) and o >= (s - b):
        oranges += 1
        
print apples
print oranges
