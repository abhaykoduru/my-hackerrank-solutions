import re
N = int(raw_input().strip())
stack = []
stack_max = None
for each in xrange(N):
    query = raw_input().strip()
    m = re.match("^(\d){1}\s*(\d*)$", query)
    choice = int(m.group(1))
    if choice == 1:
        number = int(m.group(2))
        stack.append(number)
        if number > stack_max:
            stack_max = number
    elif choice == 2:
        n = stack.pop()
        if stack_max == n:
            if stack:
                stack_max = max(stack)
            else: stack_max = None
    else:
        print stack_max
