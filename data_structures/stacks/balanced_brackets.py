#!/bin/python

import sys

open_braces = ['{', '[', '(']
close_braces = [')', ']', '}']
results = []

test_cases = int(raw_input().strip())
for each_test_case in xrange(test_cases):
    string = raw_input().strip()
    stack = []
    for char in string:
        if char in open_braces:
            stack.append(char)
        elif char in close_braces:
            top_brace = None
            if stack:
                top_brace = stack.pop()
                if ((top_brace == '{' and char != '}') or
                    (top_brace == '[' and char != ']') or
                    (top_brace == '(' and char != ')')):
                    stack.append(top_brace)
                    break
            else:
                stack.append(char)
                break
    if stack == []:
        results.append('YES')
    else:
        stack = []
        results.append('NO')

for result in results:
    print result
