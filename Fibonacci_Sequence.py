n = int(input(": "))

# Starting values
a = 0
b = 1

for i in range(1, n+1):
    print(a)
    c = a
    a += b
    b = c
