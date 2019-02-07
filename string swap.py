es (12 sloc)  250 Bytes
import re

pat = r'^[s-zA-Z]+$'

b = input()

if bool(re.match(pat, b)):
    n = len(b)
    if n % 2 != 0:
        print("Invalid")
    else:
        for i in range(0, n, 2):
            print(b[i+1] + b[i], end = "")
else:
    print("Invalid")
