import sys

sys.stdout.write()

s = {1: 5, 7: 2, 3: 4, 15: 2, -6: 4}

for i in sorted(s.items(), reverse=True):
    print(i)
