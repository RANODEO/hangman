import re

string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)

line = "123 hi 34 Hello."
f = re.findall("\d", line, re.IGNORECASE)
print(f)

t = "__one____two____three____four__"
found = re.findall("__.*?__", t)
for match in found:
    print(match)
