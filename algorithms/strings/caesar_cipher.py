# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())
temp = raw_input()
K = int(raw_input())
result = ""
for t in temp:
    if ord(t) >= 65 and ord(t) <= 90:
        ascii = ord(t) - 65
        ascii += K
        ascii = ascii % 26
        ascii += 65
        result += chr(ascii)
    elif ord(t) >= 97 and ord(t) <= 122:
        ascii = ord(t) - 97
        ascii += K
        ascii = ascii % 26
        ascii += 97
        result += chr(ascii)
    else:
        result += t
print result
