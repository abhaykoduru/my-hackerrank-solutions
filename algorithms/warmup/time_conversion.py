# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

in_time = raw_input().strip()
if re.match("((\d\d:?)*)AM$", in_time):
    temp = re.match("((\d\d:?)*)AM$", in_time).group(1)
    temp = temp.split(":")
    if temp[0] == "12":
        temp[0] = "00"
    print ":".join(temp)
else:
    temp = re.match("((\d\d:?)*)PM$", in_time).group(1)
    temp = temp.split(":")
    temp[0] = str(int(temp[0]) + 12)
    if temp[0] == "24":
        temp[0] = "12"
    print ":".join(temp)
