import time

start = time.time()

values = {}
for x in range(3, 1000):
    if x % 3 == 0:
        values[x] = x
    else:
        if x % 5 == 0:
            values[x] = x

sum = 0
for k in values:
    sum = sum + k

print(sum)
timer = str((time.time() - start)*1000.0)
print( timer + " ms")