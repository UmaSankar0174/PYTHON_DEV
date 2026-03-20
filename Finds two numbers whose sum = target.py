L = [2,7,11,15]
target = 9
s = {}
for i in L:
    d = target - i
    if d in s:
        print(d, i)
    s[i] = True